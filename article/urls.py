from django.conf.urls import url
from article.views import articles

urlpatterns = [
    url(r'^', articles),
]
