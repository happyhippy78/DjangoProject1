# Generated by Django 5.0.1 on 2024-03-06 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appPublication', '0002_alter_pubnews_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os', models.CharField(blank=True, max_length=150, null=True, verbose_name='Операционная система')),
                ('browser', models.CharField(blank=True, max_length=150, null=True, verbose_name='Браузер')),
                ('is_bot', models.BooleanField(blank=True, choices=[(True, 'Да'), (False, 'Нет')], default=False, null=True, verbose_name='Бот')),
                ('is_touch_capable', models.BooleanField(blank=True, choices=[(True, 'Да'), (False, 'Нет')], default=False, null=True, verbose_name='Поддержка сенсорного экрана')),
                ('type_device', models.CharField(blank=True, choices=[('mobile', 'телефон'), ('tablet', 'Планшет'), ('pc', 'ПК')], max_length=150, null=True, verbose_name='Тип устройства')),
                ('pub_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPublication.pubnews', verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'историю',
                'verbose_name_plural': 'Просмотры',
            },
        ),
    ]
