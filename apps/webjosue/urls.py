from django.urls import path
from .views import goku


urlpatterns = {
    path('', goku, name='wenos'),
}