# Generated by Django 5.0.6 on 2024-06-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0012_carrito_itemcarrito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tamaño',
            field=models.CharField(choices=[('grande', 'Grande'), ('pequeño', 'Pequeño')], default='grande', max_length=10),
        ),
    ]
