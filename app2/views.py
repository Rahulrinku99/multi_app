from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2_first(request):
    return HttpResponse('<h1><center>welcome to first of app2</center></h1>')


def app2_second(request):
    return HttpResponse('<h1><marquee>welcome to second of app2</marquee></h1')