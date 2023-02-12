from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request, name, mama):
    mama=0
    return render(request, "hela/index.html", {
        "name": name,
        "mama": mama
    })
