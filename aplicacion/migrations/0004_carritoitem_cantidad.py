# Generated by Django 5.0.6 on 2024-07-05 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_remove_carritoitem_cantidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carritoitem',
            name='cantidad',
            field=models.PositiveIntegerField(default=1),
        ),
    ]