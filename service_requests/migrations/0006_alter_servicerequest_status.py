# Generated by Django 3.2 on 2022-04-20 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_requests', '0005_alter_servicerequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('created', 'created'), ('waiting payment', 'waiting payment'), ('in process', 'in process'), ('canceled', 'canceled'), ('done', 'done')], max_length=25),
        ),
    ]
