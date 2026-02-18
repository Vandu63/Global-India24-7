from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('home/',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('jobs/',views.jobs),
    path('login/',views.login),
    path('news/',views.news),
    path('videos/',views.videos),
    path('faqs/',views.faqs),
    path('newsdetails/',views.newsdetail),
    path('myprofile/',views.myprofile)

]