from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello (request):
    return HttpResponse("Hello!")

def index(request):
    return HttpResponse("Hello, World. This is the index of Demoapp")