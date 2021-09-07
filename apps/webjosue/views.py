from django.shortcuts import render

# Create your views here.
def goku(request):
    return render(request, 'index.html')

def contact(request):
    return render(request,'contact.html')
