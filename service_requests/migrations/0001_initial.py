# Generated by Django 3.2 on 2022-04-19 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0006_service_integration_rout'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=25)),
                ('payment_status', models.CharField(max_length=25)),
                ('payment_method', models.CharField(max_length=25)),
                ('price', models.FloatField(blank=True, max_length=125, null=True)),
                ('user_notes', models.TextField(blank=True, null=True)),
                ('operation_notes', models.TextField(blank=True, null=True)),
                ('full_requester_name', models.CharField(max_length=255)),
                ('requester_mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('pick_up_location', models.JSONField(blank=True, default=dict, null=True)),
                ('drop_off_location', models.JSONField(blank=True, default=dict, null=True)),
                ('destination', models.CharField(blank=True, max_length=255, null=True)),
                ('hotel_name', models.CharField(blank=True, max_length=255, null=True)),
                ('check_in_date', models.DateField(blank=True, null=True)),
                ('check_out_date', models.DateField(blank=True, null=True)),
                ('number_of_rooms', models.IntegerField(blank=True, null=True)),
                ('room_type', models.CharField(blank=True, max_length=55, null=True)),
                ('number_of_adult', models.IntegerField(blank=True, null=True)),
                ('number_of_children', models.IntegerField(blank=True, null=True)),
                ('flying_from', models.CharField(blank=True, max_length=125, null=True)),
                ('flying_to', models.CharField(blank=True, max_length=125, null=True)),
                ('departure_date', models.DateField(blank=True, null=True)),
                ('returning_date', models.DateField(blank=True, null=True)),
                ('number_of_adult_passengers', models.IntegerField(blank=True, null=True)),
                ('number_of_children_passengers', models.IntegerField(blank=True, null=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_requests', to='services.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_service_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
