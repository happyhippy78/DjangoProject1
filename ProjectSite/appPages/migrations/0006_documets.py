# Generated by Django 5.0.1 on 2024-01-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPages', '0005_aboutme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название документа')),
                ('file', models.FileField(blank=True, null=True, upload_to='documents', verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'документ',
                'verbose_name_plural': 'документ',
            },
        ),
    ]
