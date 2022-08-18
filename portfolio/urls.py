from django.contrib import admin
from django.urls import path
from portfolio import views


urlpatterns = [
    path("" , views.index, name= 'portfolio'),
    path("about", views.about,name = 'about'),
    path("contact" , views.contact , name ='contact'),
    path("services" , views.services , name ='services'),
path("projects" , views.portfolio , name ='Portfolio'),
]
