
from django.conf.urls import include, url
from django.contrib import admin
from login import views as login_views

urlpatterns = [
    url(r'^login',login_views.login),
    url(r'^register',login_views.register),
    url(r'^recover',login_views.recover),
    url(r'^$', include('login.urls')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/',include('users.urls')),
    
]
