from django.urls import path
from appcoder import views



urlpatterns = [
    path('', views.inicio),
    path("cursos",views.curso_1, name= "cursos"),
    path("profesores",views.profesores),
    path("estudiantes",views.estudiantes),
    path("entregable",views.entregables),
]   
