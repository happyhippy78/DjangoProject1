from django.db import models
import datetime
import uuid
from tinymce.models import HTMLField

class PubNews(models.Model):
    content = HTMLField(
        "Содержание",
        null= False
    )
    date_time = models.DateTimeField(
        "Дата и время публикации",
        null = False,
        default = datetime.datetime.now
    )
    name_url = models.CharField(
        "Имя ссылки",
        max_length = 10,
        null= False,
    )
    def __str__(self):
        return self.name_url
    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"


    