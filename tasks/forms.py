from django import forms
from .models import Taskss

class TaskForm(forms.ModelForm):
    class Meta:
        model = Taskss
        fields = ['title','description','important']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'write a title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write a description'}),
            'important': forms.CheckboxInput (attrs={'class':'form-check-input'})
        }
        
