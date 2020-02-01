from django.conf.urls import url
from reg import views

app_name = 'reg'

urlpatterns = [
    url(r'^email/(?P<id>\d+)/$', views.email, name='email'),
    url(r'^delete/(?P<id>\d+)/$', views.DeleteView, name='delete'),
]
