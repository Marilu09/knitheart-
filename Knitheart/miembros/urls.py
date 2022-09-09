
from unicodedata import name
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('agregar', views.newMembers, name= 'agregar'),
    path('consultar', views.getMembers, name='consultar') 

]
