# Generated by Django 5.1.2 on 2024-11-10 14:34

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_tag_created_at_remove_tag_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
    ]