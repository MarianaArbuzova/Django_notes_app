from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteForm
from .models import Notes, Category
from django.db.models import Q


# створення нотатки
def create_note_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:index') # повернення на головну
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})

def index_view(request):
    notes = Notes.objects.select_related('category').all()

    q=request.GET.get('q', "").strip()
    category_id = request.GET.get('category')

    if q:
        notes = notes.filter(
            Q(title__icontains=q) |
            Q(text__icontains=q) |
            Q(category__title__icontains=q)
        )

    if category_id:
        notes = notes.filter(category_id=category_id)

    categories = Category.objects.all().order_by('title')

    context = {
        'notes': notes,
        'page_title': 'Мої нотатки',
        'categories': categories,
        'current_query': q,
        'current_category': category_id,
    }
    return render(request, 'index.html', context)

def note_detail_view(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    return render(request, 'note_detail.html', {'note': note})

def edit_note_view(request, pk):
    note = Notes.objects.get(pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form, 'note': note})

def delete_note_view(request, pk):
    note = get_object_or_404(Notes, pk=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('notes:index')
    return render(request, 'delete_note_confirm.html', {'note': note})