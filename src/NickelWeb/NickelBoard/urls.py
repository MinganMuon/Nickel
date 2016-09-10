from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gsb/', views.gsb, name='ajax-getstartingboard'),
    url(r'^iswon/', views.iswon, name='ajax-iswon'),
    url(r'^gpmoves/', views.gpmoves, name='ajax-getpossiblemoves'),
]
