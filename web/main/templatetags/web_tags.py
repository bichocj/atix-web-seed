from django import template
from main.models import Post, Category
from django.core.paginator import Paginator

register = template.Library()


@register.simple_tag
def get_last_posts(post_per_page, page):
    posts = Post.objects.all().order_by('-publish_at')
    paginator = Paginator(posts, post_per_page)
    return paginator.page(page)


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def get_post_by_id(id):
    return Post.objects.get(id=id)
