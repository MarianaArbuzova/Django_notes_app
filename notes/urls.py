from django.urls import path
from .views import index_view, create_note_view, note_detail_view, edit_note_view, delete_note_view


app_name = 'notes'

urlpatterns = [
    path('', index_view, name='index'),
    path('create/', create_note_view, name='create_note'),
    path('<int:pk>/', note_detail_view, name='note_detail'),
    path('<int:pk>/edit/', edit_note_view, name='edit_note'),
    path('<int:pk>/delete/', delete_note_view, name='delete_note'),
]