# Generated by Django 5.1.2 on 2024-11-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_product_dimensions_product_thumbnail_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='products', to='myapp.tag'),
        ),
    ]
