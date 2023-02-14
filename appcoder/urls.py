from django.urls import path
from appcoder import views



urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path("cursos",views.curso_1, name= "curso"),
    path("profesores",views.profesores, name = "profesores"),
    path("estudiantes",views.estudiantes, name = "estudiantes"),
    path("entregable",views.entregables, name = "entregables"),
]   
