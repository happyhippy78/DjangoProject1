from django.db import models
from appPublication.models import PubNews


class StaticLink(models.Model):
    pub_news = models.ForeignKey(
        PubNews,
        verbose_name = "Публикация",
        on_delete = models.CASCADE,
        null = False,
    )
    os = models.CharField(
        "Операционная система",
        null=True,
        blank=True,
        max_length = 150
    )
    browser = models.CharField(
        "Браузер",
        null=True,
        blank=True,
        max_length = 150
    )
    is_bot = models.BooleanField(
        "Бот",
        choices = [
            (True, "Да"),
            (False, "Нет"),
        ],
        default = False, 
        null = True,
        blank = True,
    )
    is_touch_capable = models.BooleanField(
        "Поддержка сенсорного экрана",
        choices = [
            (True, "Да"),
            (False, "Нет"),
        ],
        default = False, 
        null = True,
        blank = True,
    )
    type_device = models.CharField(
        "Тип устройства",
        choices = [
            ('mobile', "телефон"),
            ('tablet', "Планшет"),
            ('pc', "ПК"),
        ],
        null=True,
        blank=True,
        max_length = 150
    )
    def __str__(self):
        return self.pub_news.name_url
    class Meta:
        verbose_name = "историю"
        verbose_name_plural = "Просмотры"
