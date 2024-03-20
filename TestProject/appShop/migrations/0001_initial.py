# Generated by Django 5.0.1 on 2024-03-20 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProducrShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Имя товара')),
                ('count', models.IntegerField(default=0, verbose_name='Количество товара на складе')),
                ('price', models.FloatField(default=0, verbose_name='Цена товара')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
