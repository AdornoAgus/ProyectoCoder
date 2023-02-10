from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import curso
from django.template import Template, Context
# Create your views here.

def inicio(self):
    miHtml=open("C:/Users/Admin/Desktop/PythonProyecto1/ProyectoCoder/CarpetaGitHub/ProyectoCoder/appcoder/template/appcoder/inicio.html")
    plantilla= Template(miHtml.read())
    miHtml.close()
    miContexto=Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def curso_1(self):
    miHtml=open("C:/Users/Admin/Desktop/PythonProyecto1/ProyectoCoder/CarpetaGitHub/ProyectoCoder/appcoder/template/appcoder/cursos.html")
    plantilla= Template(miHtml.read())
    miHtml.close()
    miContexto=Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def profesores(self):
    miHtml=open("C:/Users/Admin/Desktop/PythonProyecto1/ProyectoCoder/CarpetaGitHub/ProyectoCoder/appcoder/template/appcoder/profesores.html")
    plantilla= Template(miHtml.read())
    miHtml.close()
    miContexto=Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def entregables(self):
    miHtml=open("C:/Users/Admin/Desktop/PythonProyecto1/ProyectoCoder/CarpetaGitHub/ProyectoCoder/appcoder/template/appcoder/entregables.html")
    plantilla= Template(miHtml.read())
    miHtml.close()
    miContexto=Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def estudiantes(self):
    miHtml=open("C:/Users/Admin/Desktop/PythonProyecto1/ProyectoCoder/CarpetaGitHub/ProyectoCoder/appcoder/template/appcoder/estudiantes.html")
    plantilla= Template(miHtml.read())
    miHtml.close()
    miContexto=Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)
   

    
