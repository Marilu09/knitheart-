from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed

def index (request):
    return HttpResponse ("Hola, mundo")

def newMembers (request):
    if request.method == 'POST':
        return HttpResponse ("va a agregar un nuevo miembro")
    else:
        return HttpResponseNotAllowed (['POST'],"metodo invalido")

def getMembers (request):
    if request.method == 'GET':
        return HttpResponse ("esta es la inf de los miembros")
    else:
        return HttpResponseNotAllowed (['GET'],"metodo invalido")        


