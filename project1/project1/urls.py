
from django.conf.urls import include, url
from django.contrib import admin
from login import views as login_views
from course import views as course_views
from users import views as user_views

urlpatterns = [
    url(r'^login',login_views.login),
    url(r'^register',login_views.register),
    url(r'^recover',login_views.recover),
    url(r'^$', include('login.urls')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/',include('users.urls')),
    url(r'^user/',user_views.index),
    url(r'^course/',course_views.index)

    
]
