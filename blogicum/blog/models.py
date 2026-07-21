from django.db import models
from core.models import PublishedModel
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(PublishedModel):
    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание категории')
    slug = models.SlugField('Слаг')


class Location(PublishedModel):
    name = models.CharField('Локация', max_length=256)


class Post(PublishedModel):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Текст поста')

    pub_date = models.DateTimeField(
        'Дата публикации',
        help_text='Введите дату публикации поста'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
