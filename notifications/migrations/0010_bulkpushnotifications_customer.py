# Generated by Django 3.2 on 2022-09-05 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20220824_2222'),
        ('notifications', '0009_delete_mydevice'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkpushnotifications',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer'),
        ),
    ]
