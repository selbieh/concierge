# Generated by Django 3.2 on 2022-03-16 22:08

from django.db import migrations, models
import django.db.models.deletion
import services.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0003_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=services.models.upload_service_image, verbose_name='image')),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_services', to='customers.category')),
            ],
        ),
    ]
