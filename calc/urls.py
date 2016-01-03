from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^participants/$', views.participants),
    url(r'^calculator/$', views.calculator),
    url(r'^compute/$', views.compute),
]