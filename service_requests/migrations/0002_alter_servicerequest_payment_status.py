# Generated by Django 3.2 on 2022-04-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='payment_status',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
