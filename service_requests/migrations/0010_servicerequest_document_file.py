# Generated by Django 3.2 on 2022-08-30 07:09

from django.db import migrations, models
import service_requests.models


class Migration(migrations.Migration):

    dependencies = [
        ('service_requests', '0009_gifterycallback_giftry_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='document_file',
            field=models.FileField(blank=True, null=True, upload_to=service_requests.models.upload_image),
        ),
    ]