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

class AboutMe(models.Model):
    fio = models.CharField (
        "ФИО", 
        max_length = 200,
        null = False
    )
    desc = models.TextField (
        "Описание", 
        null = False
    )
    expert = models.CharField (
        "Должность", 
        max_length = 250,
        null = False
    )
    photo = models.ImageField (
        "Изображение", 
        null = False,
        upload_to='about-me'
    )
    def __str__(self):
        return self.fio
    def clean(self):
        super().clean()
        if AboutMe.objects.count() > 1 and not self.ph:
            raise ValidationError("Максимальное количество достигнуто. Всего доступно: 1")
    class Meta:
        verbose_name = "информацию"
        verbose_name_plural = "Обо Мне"

class Documets(models.Model):
    title = models.CharField(
        "Название документа",
        null= False,
        max_length = 100
    )
    file = models.FileField(
        "Документ",
        null=True,
        blank=True,
        upload_to="documents"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "документ"     # для кнопки
        verbose_name_plural = "документ"  # для отображения панели