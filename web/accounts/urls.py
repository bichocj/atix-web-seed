from django.conf.urls import include, url
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm
from django.contrib.auth.views import (password_reset_complete, password_reset_confirm,
                                       password_reset_done, password_reset, login, logout)

from . import views

password_reset_patterns = [
    url(r'^done/$', password_reset_complete, {
        'template_name': 'accounts/password/password_reset_complete.html',
        'extra_context': {
            'title': 'Password reset complete',
        }
    }, name='password_reset_complete'),
    url(r'^reset/done/$', password_reset_done, {
        'template_name': 'accounts/password/password_reset_done.html',
        'extra_context': {
            'title': 'Password reset done',
        }
    }, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {
        'set_password_form': SetPasswordForm,
        'template_name': 'accounts/password/password_reset_confirm.html',
        'post_reset_redirect': '/accounts/password/done/',
        'extra_context': {
            'title': 'Password reset confirm',
        }
    }, name='password_reset_confirm'),
    url(r'^reset/$', password_reset, {
        'password_reset_form': PasswordResetForm,
        'template_name': 'accounts/password/password_reset_form.html',
        'email_template_name': 'accounts/email/email_reset.html',
        'post_reset_redirect': '/accounts/password/reset/done/',
        'extra_context': {
            'title': 'Password Reset',
        }
    }, name='password_reset'),
]

profile_patterns = [
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup')
]

urlpatterns = [
    url(r'^', include(profile_patterns)),
    url(r'^password/', include(password_reset_patterns)),
]
