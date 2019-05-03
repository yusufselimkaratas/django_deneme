from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hoşgeldin kardo.")

# Create your views here.
