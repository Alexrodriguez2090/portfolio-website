from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request.path)
    return render(request, "portfolio.html")