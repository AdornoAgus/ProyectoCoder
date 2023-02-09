from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import curso

# Create your views here.
def inicio(request):
    return render(request,"appcoder/inicio.html")
    #return HttpResponse("vista inicio")

def curso_1(request):
    return render(request,"appcoder/cursos.html")
    #return HttpResponse("vista cursos")

def profesores(request):
    return render(request,"appcoder/profesores.html")
    #return HttpResponse("vista Profesores")

def entregables(request):
    return render(request,"appcoder/entregables.html")
    #return HttpResponse("vista entregas")

def estudiantes(request):
    return render(request,"appcoder/estudiantes.html")
    #return HttpResponse("vista estudiantes")
   

    
