from django.contrib import admin
from django.conf.urls import url
from . import views
urlpatterns = [
url('login/', views.login, name='login'),
url('profile/', views.profile, name='profile'),
url('logout/', views.logout, name='logout'),
]