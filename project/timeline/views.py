from django.shortcuts import render
from django.http import HttpResponse

def index(requests):
    return HttpResponse('This is timeline/index page')