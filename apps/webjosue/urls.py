from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('detalles/', detalles, name='detalles'),
    path('departament/', departament, name='departament'),
    path('doctor/', doctor, name='doctor'),
    path('elements/', elements, name='elements'),
    path('contact/', contact, name='contact')
]
