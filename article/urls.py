from django.conf.urls import url


urlpatterns = [

    url(r'^$', 'article.views.blog_index', name='blog_index'),
    url(r'^home$', 'article.views.home', name='home'),
    url(r'^detail/(?P<pk>[0-9]+)/$', 'article.views.detail', name='detail'),
    url(r'^index$', 'article.views.index', name='index'),
    #url(r'^detail/(?P<pk>[0-9]+)$', 'article.views.detail', name='detail')
]