from django.shortcuts import render
from django.http import HttpResponse
from .models import Perfil

def enviar(request):
    perfil=Perfil.objects.all() 
    return render(request,'index.html',context={'perfil':perfil})