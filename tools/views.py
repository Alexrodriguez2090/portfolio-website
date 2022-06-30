from django.shortcuts import render
from django.http import HttpResponse


def apicalls(request):
    return render(request, "api-calls.html")