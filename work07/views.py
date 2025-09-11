from django.http import HttpResponse
from django.shortcuts import render


def top(request):
    return render(request, "work07/top.html")


def omikuji(request):
    return render(request, "work07/omikuji.html")


# Create your views here.
