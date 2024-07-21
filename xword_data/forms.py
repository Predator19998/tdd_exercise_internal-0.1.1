from django import forms
from .models import Clue

class DrillForm(forms.Form):
    clue_id = forms.IntegerField(widget=forms.HiddenInput)
    answer = forms.CharField(max_length=100, label='Your answer')