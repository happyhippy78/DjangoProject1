# Generated by Django 5.0.1 on 2024-01-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appPages', '0002_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер')),
            ],
        ),
    ]
