from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    allclientes = cliente.objects.all()
    allmedico = medico.objects.all()
    return render(request, 'index.html',{'allclientes':allclientes},{'allmedico':allmedico})

def about(request):
    return render(request,'about.html')

def departament(request):
    return render(request,'department.html')

def doctor(request):
    allmedico = medico.objects.all()
    return render(request,'doctor.html',{'allmedico':allmedico})


def contact(request):
    return render(request,'contact.html')