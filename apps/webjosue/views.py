from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    allclientes = cliente.objects.all()
    return render(request, 'index.html',{'allclientes':allclientes})

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def detalles(request):
    return render(request,'detalles.html')

def departament(request):
    return render(request,'department.html')

def doctor(request):
    return render(request,'doctor.html')

def elements(request):
    return render(request,'elements.html')

def contact(request):
    return render(request,'contact.html')