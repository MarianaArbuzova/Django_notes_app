from django.db import models


class Category(models.Model):
    # Для категорій нотаток: Робота, Особисте, Покупки...
    # назва категорії
    title = models.CharField(
        max_length=200,
        verbose_name='Назва категорії'
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self) -> str:
        return self.title

class Notes(models.Model):
    # Для нотаток. Дата нагадування, текст...
    title = models.CharField(
        max_length=200,
        verbose_name='Назва нотатки'
    )

    # основний текст зміст нотатки
    text = models.TextField(
        verbose_name='Текст'
    )

    # дата нагадування
    reminder = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата нагадування'
    )
    # звязок з категорією (ключ)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,  # якщо видалять, то зникнуть нотатки
        related_name="notes",      # для доступу до category.notes.all()
        verbose_name='Категорія'

    )

    class Meta:
        ordering = ["-reminder", "title"]  #сортування, де нагадування ближче
        verbose_name = 'Нотатка'
        verbose_name_plural = 'Нотатки'

    def __str__(self) -> str:
        return f"{self.title} ({self.category.title})"
