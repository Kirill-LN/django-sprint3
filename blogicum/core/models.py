from django.db import models

# Create your models here.
class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField('Опубликовано', default=True)
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        abstract = True