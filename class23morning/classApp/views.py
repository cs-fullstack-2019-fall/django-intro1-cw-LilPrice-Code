from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is a bad request. Start with the music route.")

def music(request):
    return HttpResponse("Lukas,Script, or Macklemore")

def lukas(request):
    return HttpResponse("Lukas Graham")

def script(request):
    return HttpResponse("The Script")

def mack(request):
    return HttpResponse("Macklemore")
