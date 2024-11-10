# Generated by Django 5.1.2 on 2024-11-10 15:17

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_product_search_vector'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='product',
            name='myapp_produ_title_391dd3_idx',
        ),
        migrations.AddIndex(
            model_name='product',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='myapp_produ_search__67bd3d_gin'),
        ),
    ]
