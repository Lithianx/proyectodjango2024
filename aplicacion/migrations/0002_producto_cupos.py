# Generated by Django 5.0.6 on 2024-07-05 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cupos',
            field=models.PositiveIntegerField(default=30, verbose_name='Cupos'),
        ),
    ]