# Generated by Django 3.2 on 2022-05-26 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_service_integration_rout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
