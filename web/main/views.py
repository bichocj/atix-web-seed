from django.shortcuts import render

from main.models import Post


def render_page(request, page_slug):
    page = request.GET.get('page', 1)
    try:
        return render(request, 'main/' + page_slug + '.html', locals())
    except:
        return not_found(request)


def render_home(request):
    return render_page(request, 'index')


def not_found(request):
    return render(request, 'main/common/404.html', locals(), status=404)


def bad_request(request):
    return render(request, "main/common/500.html", locals(), status=500)


def show_post(request,post_id):    
    return render(request,"main/blog-post.html", locals())