from django.shortcuts import render

from django.http import HttpResponse

def index(req):
    return HttpResponse("Hello, This is your first page.")

# Create your views here.
