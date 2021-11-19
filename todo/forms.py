from django.forms import ModelForm
from .models import assignment
from django import forms


class forme(forms.Form):
    dish=forms.CharField(max_length=50)

class forme2(forms.Form):
    num = forms.IntegerField(label="How many tables do you want ?")
