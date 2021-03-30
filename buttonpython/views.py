from django.shortcuts import render
import requests
import os
from django.http import HttpResponse
from subprocess import run, PIPE
import sys
from datetime import datetime
from datetime import date

sys.path.insert(1, 'backend/')
from GenerarExcel import GenerarExcel

generarExcel = GenerarExcel()


def __init__(self):
        sql = "vacio"

def button(request):
    return render(request, 'home.html')


def output(request):
    os.system('python backend/main.py')
    return HttpResponse("OK")

def output2(request):
    os.system('python backend/main2.py')
    return HttpResponse("OK")

def genexcel(request):
    generarExcel.generarCarteleraExcel(date.today())
    return HttpResponse("OK")

def genasientos(request):
    generarExcel.genrAsientosOcupadosPeliculaExcel(date.today())
    return HttpResponse("OK")

def geninfo(request):
    generarExcel.genrInfoPeliculaExcel(date.today())
    return HttpResponse("OK")

def external(request):
    fecha = request.POST.get('param')
    generarExcel.genrAsientosOcupadosPeliculaExcel(fecha)
    return HttpResponse("OK")

def externalCartel(request):
    fecha = request.POST.get('param')
    generarExcel.generarCarteleraExcel(fecha)
    return HttpResponse("OK")

def externalInfo(request):
    fecha = request.POST.get('param')
    generarExcel.genrInfoPeliculaExcel(fecha)
    return HttpResponse("OK")
    