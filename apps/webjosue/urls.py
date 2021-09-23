from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('departament/', departament, name='departament'),
    path('doctor/', doctor, name='doctor'),
    path('contact/', contact, name='contact')
]
