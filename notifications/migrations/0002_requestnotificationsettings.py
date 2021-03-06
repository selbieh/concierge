# Generated by Django 3.2 on 2022-04-20 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestNotificationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_status', models.CharField(choices=[('initiated', 'initiated'), ('paid', 'paid'), ('not required', 'not required')], max_length=25)),
                ('new_status', models.CharField(choices=[('initiated', 'initiated'), ('paid', 'paid'), ('not required', 'not required')], max_length=25)),
                ('message', models.CharField(max_length=125)),
            ],
        ),
    ]
