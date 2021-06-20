from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def drill(request):
    return HttpResponse("drill")


def answer(request, pk):
    
    return HttpResponse("answer")
