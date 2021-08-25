
from django.contrib import admin
from django.urls import path, include
from home import views
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import RedirectView
from uploader.views import upload,movieDetail,movieCategory

urlpatterns = [

    path('', views.netflix, name='netflix'),
    path('home/', views.home, name='home'),
    path('about', views.about, name='about'),
    path('upload/', upload, name='upload'),
    path('spidermannwh', views.spidermannwh, name='spidermannwh'),
    path('upload/', upload, name='upload'),
    path('movie/<str:movieId>/',movieDetail),
    path('movie/category/<str:category>/',movieCategory),
    path('login', views.login, name='login'),

   ]