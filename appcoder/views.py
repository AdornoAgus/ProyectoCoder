from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import curso

# Create your views here.


def curso_1(self):
    curso_1=curso(nombre= "desarrollo web", comision=25)
    curso_1.save()
    documento_texto = f"---> curso: {curso_1.nombre} comision: {curso_1.comision}"
    return HttpResponse(documento_texto)
