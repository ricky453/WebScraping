from django.shortcuts import render
import requests
import os
from django.http import HttpResponse


def button(request):
    return render(request, 'home.html')


def output(request):
    os.system('python backend/main.py')
    return HttpResponse("OK")