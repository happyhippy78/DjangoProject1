# Generated by Django 5.0.1 on 2024-03-06 18:09

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appPublication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pubnews',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Содержание'),
        ),
    ]
