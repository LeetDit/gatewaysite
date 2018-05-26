from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'gatewaymotel/index.html')

def about(request):
    return render(request, 'gatewaymotel/index1.html')

def attractions(request):
    return render(request, 'gatewaymotel/index2.html')

def room(request):
    return render(request, 'gatewaymotel/index3.html')

def contact(request):
    return render(request, 'gatewaymotel/index4.html')
