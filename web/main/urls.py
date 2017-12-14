from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^blog/(?P<post_id>\d+)/$', views.show_post, name='show_post'),
    url(r'^(?P<page_slug>[\w\.-]+)/$', views.render_page),
    url(r'^$', views.render_home),
]