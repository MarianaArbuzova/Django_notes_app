from django.urls import path
from . import views


app_name = 'notes'

urlpatterns = [
    # path('') означає головну сторінку застосунку
    # Вона викликає функцію views.index_view, і ми даємо їй ім'я 'index'
    path('', views.index_view, name='index'),
]