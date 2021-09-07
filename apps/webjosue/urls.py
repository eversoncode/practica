from django.urls import path
from .views import *


urlpatterns = {
    path('', goku, name='wenos'),
    path('', contact, name= 'contact')
}