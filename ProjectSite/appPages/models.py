from django.db import models
from django.core.exceptions import ValidationError
import datetime


class ContentBanner(models.Model):
    title = models.CharField (
        "Название",
        max_length = 100,
        null = False
    )
    desc = models.TextField(
        "Описание",
        null = False
    )
    number = models.IntegerField(
        "Порядковый номер",
        null = True,
        blank = True
    )
    def clean(self):
        super().clean()
        if ContentBanner.objects.count() > 3 and not self.pk:
            raise ValidationError("Максимальное количество достигнуто. Всего доступно: 3")
        
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'контент'
        verbose_name_plural = 'Баннер'