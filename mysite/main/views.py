from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    return HttpResponse("One stop shop for Blockchain Roadmaps")
