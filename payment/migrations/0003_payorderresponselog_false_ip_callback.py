# Generated by Django 3.2 on 2022-06-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20220619_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='payorderresponselog',
            name='false_ip_callback',
            field=models.BooleanField(default=False),
        ),
    ]
