from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name = 'web'
urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^like$', views.like, name='like'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    url(r'^post/(?P<post_id>[-\d]+)/delete/$', views.post_delete, name="post_delete"),
    url(r'^search$', views.search, name="search"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
