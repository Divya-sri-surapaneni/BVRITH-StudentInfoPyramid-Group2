from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^next/$', views.next, name='next'),
    url(r'^success/$', views.success, name='success'),
    url(r'^display/$', views.display, name='display'),
]
