from django.http import HttpResponse
from django.shortcuts import render


def html(request):
    context = "ryuto"
    return render(request, "work05/index.html", {"my_name": context})


def index(request):
    return HttpResponse("This is the top page of work05.")


def top(request):
    return HttpResponse("This is the top page of work05.")


def list(request):
    return HttpResponse("This is the list page of work05.")


# Create your views here.
