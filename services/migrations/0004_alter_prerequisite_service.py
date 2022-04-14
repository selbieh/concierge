# Generated by Django 3.2 on 2022-04-14 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20220414_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prerequisite',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prerequisites', to='services.service'),
        ),
    ]
