from django.conf.urls import url
from farmers import views
urlpatterns = [
    url(r'^$',views.Farmer_Organ,name = 'farmer'),
    url(r'^email/(?P<id>\d+)/$', views.email, name='email'),
    url(r'^delete/(?P<id>\d+)/$', views.DeleteView, name='delete'),
    url(r'^addressupdate/$', views.addressupdate, name='addressupdate'),

]
