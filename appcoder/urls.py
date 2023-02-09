from django.urls import path
from appcoder import views



urlpatterns = [
    path('', views.inicio),
    path("cursos",views.curso_1,name="Cursos"),
    path("Profesores",views.profesores),
    path("Estudiantes",views.estudiantes),
    path("Eentregable",views.entregables),
]   
