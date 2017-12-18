from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import Http404

from .models import Config


def signup(request):    
    if not Config.get().can_anyone_register:
        raise Http404

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', locals())


def message(request, code):
    if code == 'password_reset':
        message = _(
            '<strong>We have sent you an email!</strong> Please, follow the instructions to reset your password.')
        # messages.add_message(request, messages.INFO, message)
        return render(request, 'accounts/echo.html', locals())
        # return redirect(reverse('accounts:password_reset'))

    if code == 'password_reset_confirm':
        messages.add_message(request, messages.INFO, _(
            '<strong>Success!</strong> You have changed your password.'))
        return redirect(reverse('accounts:login'))

    if code == 'password_change_done':
        messages.add_message(request, messages.INFO, _(
            '<strong>Success!</strong> You have changed your password.'))
        return redirect(reverse('accounts:password_change'))

    return redirect(reverse('accounts:profile_edit'))
