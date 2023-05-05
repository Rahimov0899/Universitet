from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def ustozlar(request):
    if request.method=='POST':
        Ustoz.objects.create(
            ism=request.POST.get('ism'),
            jins=request.POST.get('j'),
            yosh=request.POST.get('yosh'),
            daraja=request.POST.get('d'),
            fan=Fan.objects.get(id=request.POST.get('fan'))

        )
        return redirect("/ustozlar/")
    soz=request.GET.get('qidiruv')
    if soz=='' or soz is None:
       content={
           "ustozlar":Ustoz.objects.all(),
           "fan":Fan.objects.all()

        }
    else:

        content={
            "ustozlar":Ustoz.objects.filter(ism__contains=soz)
        }
    return render(request,"unversitet.html",content)


def ustoz(request,id):
    Ustoz.objects.get(id=id).delete()
    return redirect("/ustozlar/")

def fanlar(request):
    if request.method=='POST':
        Fan.objects.create(
            nom=request.POST.get('nom'),
            asosiy=request.POST.get('asosiy'),
            yonalish=Yonalish.objects.get(id=request.POST.get('y'))

        )
        return redirect("/fanlar/")
    soz=request.GET.get('qidiruv')
    if soz=='' or soz is None:
       content={
           "fanlar":Fan.objects.all(),
           "yonalish":Yonalish.objects.all()

        }
    else:

        content={
            "fanlar":Fan.objects.filter(ism__contains=soz)
        }
    return render(request,"fan.html",content)


def fan(request,id):
    Fan.objects.get(id=id).delete()
    return redirect("/fanlar/")

def yonalishlar(request):
    if request.method=='POST':
        Yonalish.objects.create(
            nom=request.POST.get('nom'),
            aktiv=request.POST.get('aktiv'),

        )
        return redirect("/yonalish/")
    soz=request.GET.get('qidiruv')
    if soz=='' or soz is None:
       content={
           "yonalish":Yonalish.objects.all()

        }
    else:

        content={
            "yonalish":Yonalish.objects.filter(ism__contains=soz)
        }
    return render(request,"yonalish.html",content)


def yonalish(request,id):
    Yonalish.objects.get(id=id).delete()
    return redirect("/yonalish/")