# Generated by Django 5.0.6 on 2024-06-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_producto_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
