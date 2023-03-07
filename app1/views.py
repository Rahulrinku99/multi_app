from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_app1(request):
    return HttpResponse('<h2>welcome to app1</h2>')


def Second_app1(request):
    return HttpResponse('<h2>welcome to second app</h2>')