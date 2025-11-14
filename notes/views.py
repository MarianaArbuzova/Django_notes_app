from django.shortcuts import render
from notes.models import Notes

def index_view(request):
    notes = Notes.objects.select_related('category').all()
    context = {
        'notes': notes,
        'page_title': 'Мої нотатки'
    }
    return render(request, 'index.html', context)