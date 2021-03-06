# Generated by Django 3.2 on 2022-04-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20220420_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestnotificationsettings',
            name='new_status',
            field=models.CharField(choices=[('created', 'created'), ('in process', 'in process'), ('canceled', 'canceled'), ('done', 'done')], max_length=25),
        ),
        migrations.AlterField(
            model_name='requestnotificationsettings',
            name='previous_status',
            field=models.CharField(choices=[('created', 'created'), ('in process', 'in process'), ('canceled', 'canceled'), ('done', 'done')], max_length=25),
        ),
    ]
