from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def ustoz(request):
    nom=request.GET.get('qidiruv')
    if nom=="" or nom is None:
        content={
        "ustoz":Ustoz.objects.all()
    }
    else:
        content={
        "ustoz":Ustoz.objects.filter(ism__contains=nom)
    }
    return render(request,"unversitet.html",content)

def tralaba(request):
    return HttpResponse("<h1>Bobur</h1>")
