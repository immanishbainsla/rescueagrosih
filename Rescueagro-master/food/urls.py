"""food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from reg import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'login_success/$', views.login_success, name='login_success'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^farmers/', include('farmers.urls')),
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^$',views.base,name = 'base'),
    url(r'^signup',views.register,name = 'register'),
    url(r'^users/', include('reg.urls')),
    url(r'^home/',views.home,name = "home"),
    url(r'^login/',auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    url(r'^logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    # url(r'^password-reset/',auth_views.PasswordResetView.as_view(template_name = 'password_reset.html'),name = 'password_reset'),
    # url(r'^password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name =  'password_reset_done.html'), name='password_reset_done'),
    # url(r'^password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name =  'password_reset_confirm.html'), name='password_reset_confirm'),


    url(r'^index/',views.index,name = "index"),


]
