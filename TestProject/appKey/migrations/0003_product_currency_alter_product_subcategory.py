# Generated by Django 5.0.1 on 2024-01-31 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appKey', '0002_remove_product_category_subcategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('RU', 'Рублей'), ('USD', 'Доллары'), ('CHINA', 'Юани'), ('EU', 'Евро')], default='RU', max_length=50, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='appKey.subcategory', verbose_name='Подкатегория'),
        ),
    ]
