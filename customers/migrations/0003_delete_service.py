# Generated by Django 3.2 on 2022-03-16 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_category_service'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Service',
        ),
    ]
