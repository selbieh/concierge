# Generated by Django 3.2 on 2022-06-20 07:52

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service_requests', '0007_auto_20220526_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='number_of_adult_passengers',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='number_of_children_passengers',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='doctor_name',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='hospital_or_clinic_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='GifteryCallback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('product_list', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(default=dict), size=None)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]