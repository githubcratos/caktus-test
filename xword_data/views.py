from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseNotFound
from .models import Puzzle, Entry, Clue
from django.contrib import messages
# from django.urls import reverse


# Create your views here.
def drill(request):
    # Testing Reverse Routing.
    # found = reverse('xword-drill') 
    # print(found)

    # set error to false
    is_error = False


    if request.method == 'POST':
        answer = request.POST.get('answer')
        clue_id = request.POST.get('clue_id')
        clue = Clue.objects.get(pk=clue_id)
        if clue.entry.entry_text == answer.upper():
            messages.success(request, "Correct!!!")
            return redirect('xword-answer', pk=clue.pk)
        is_error = True
    else:
        clue = Clue.objects.order_by('?').first()
    context={
        'rand_clue': clue,
        'clue_id':clue.id,
        'is_error': is_error
    }
    return render(request, 'xword/drill.html', context)


def answer(request, pk):
     # check if in DB
    check = Clue.objects.filter(pk=pk).exists()
    if not check:
        return HttpResponseNotFound("Data Not Found")

    clue = Clue.objects.get(pk=pk)
    context={
            'clue': clue,
            'clue_id': clue.id,
            'text': 'only appearance of this clue'
        }
    return render(request, 'xword/answer.html', context)
