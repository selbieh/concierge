# Generated by Django 3.2 on 2022-04-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_requests', '0003_auto_20220419_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('in process', 'in process'), ('canceled', 'canceled'), ('DONE', 'DONE')], max_length=25),
        ),
    ]