# Generated by Django 3.2 on 2022-05-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0006_auto_20220508_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkpushnotifications',
            name='redirect_to',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='usersavednotifications',
            name='redirect_obj',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
