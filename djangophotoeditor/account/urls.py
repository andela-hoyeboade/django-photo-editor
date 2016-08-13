from django.conf.urls import include, url

from account import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^photos/$', views.PhotosView.as_view(), name='photos')
]
