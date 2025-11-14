from django import forms
from .models import Notes


class NoteForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ['title', 'text', 'reminder', 'category']

        labels = {
            'title': 'Назва',
            'text': 'Текст',
            'reminder': 'Нагадування',
            'category': 'Категорія'
        }

        # стилізація форми
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'reminder': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }