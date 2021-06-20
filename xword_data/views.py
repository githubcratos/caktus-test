from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def drill(request):
    context={}
    return render(request, 'xword/answer.html', context)


def answer(request, pk):
    context={}
    return render(request, 'xword/answer.html', context)
