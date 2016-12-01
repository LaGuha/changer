from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.main, name='main'),
   
     #url(r'^lab5/^$', views.lab5, name='lab5'),
]