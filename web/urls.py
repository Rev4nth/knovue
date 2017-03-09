from django.conf.urls import url

from . import views

app_name = 'web'
urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
]
