# Generated by Django 3.2 on 2022-04-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_requests', '0004_alter_servicerequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('in process', 'in process'), ('canceled', 'canceled'), ('done', 'done')], max_length=25),
        ),
    ]
