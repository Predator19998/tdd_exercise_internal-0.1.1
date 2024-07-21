from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Clue, Entry
from .forms import DrillForm

def drill_view(request):
    if request.method == 'POST':
        form = DrillForm(request.POST)
        if form.is_valid():
            clue_id = form.cleaned_data['clue_id']
            answer = form.cleaned_data['answer']
            clue = get_object_or_404(Clue, pk=clue_id)
            if clue.entry.entry_text.lower() == answer.lower():
                return redirect('xword-answer', clue_id=clue.id)
            else:
                return render(request, 'drill.html', {
                    'form': form,
                    'clue': clue,
                    'error_message': 'Your answer is not correct.',
                    'clue_id': clue.id,  # Add clue_id to context
                })
    else:
        clue = Clue.objects.order_by('?').first()
        form = DrillForm(initial={'clue_id': clue.id})
    return render(request, 'drill.html', {'form': form, 'clue': clue, 'clue_id': clue.id})  # Add clue_id to context

def answer_view(request, clue_id):
    clue = get_object_or_404(Clue, pk=clue_id)
    other_entries = Clue.objects.filter(clue_text=clue.clue_text).exclude(id=clue_id)
    return render(request, 'answer.html', {
        'clue': clue,
        'other_entries': other_entries,
    })