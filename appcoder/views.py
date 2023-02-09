from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import curso

# Create your views here.
def inicio(request):
    return HttpResponse("vista inicio")

def curso_1(request):
    return HttpResponse("vista cursos")

def profesores(request):
    return HttpResponse("vista Profesores")

def entregables(request):
    return HttpResponse("vista entregas")

def estudiantes(request):
    return HttpResponse("vista estudiantes")
   

    
