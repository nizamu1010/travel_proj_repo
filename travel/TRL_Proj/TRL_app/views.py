from django.shortcuts import render
from django.http import HttpResponse
from . models import place,team 

def home(request):
    obj = place.objects.all()
    details = team.objects.all()
    return render(request,'index.html',{'res': obj,'det':details})

