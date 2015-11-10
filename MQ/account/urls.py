from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^home/', 'account.views.handle_login',name="home"),
  
]