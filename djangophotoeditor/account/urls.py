from django.conf.urls import include, url

from account import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
