from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Hello Django')

def create(request):
    return HttpReponse('create')

def read(request):
    return HttpReponse('Read')


# Create your views here.
