from django.conf.urls import url
from article.views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^articles/$', articles, name='articles'),
    url(r'^articles/page/(\d+)/$', articles, name='articles_page'),
    url(r'^article/(?P<art_id>\d+)/$', article, name='article'),

]


