import email
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Members

def index (request):
    return HttpResponse ("Hola, mundo")

def newMembers (request):
    if request.method == 'POST':
        data = json.loads(request.body)
        member = Members( 
            name = data ["name"],
            email= data ["email"]
        )
        member.save()

        return HttpResponse ("va a agregar un nuevo miembro")
    else:
        return HttpResponseNotAllowed (['POST'],"metodo invalido")

def getMembers (request):
    if request.method == 'GET':
        members = Members.objects.all()
        allMembersData = []
        for x in members:
            data = {"id": x.id, "name": x.name, "email": x.email}
            allMembersData.append(data)
        dataJson = json.dumps(allMembersData)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed (['GET'],"metodo invalido")        


