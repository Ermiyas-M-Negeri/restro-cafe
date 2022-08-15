# Generated by Django 4.0.4 on 2022-08-09 04:59

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('deleted', 'Deleted')], db_index=True, default='draft', max_length=50, verbose_name='Status')),
                ('name', models.CharField(db_index=True, max_length=120, verbose_name='Name')),
                ('category', models.CharField(choices=[('hot', 'Hot'), ('cold', 'Cold'), ('bagel', 'Bagel')], db_index=True, default='others', max_length=14, verbose_name='Category')),
                ('price', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Price')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Datetime')),
            ],
            options={
                'db_table': 'item',
            },
        ),
    ]
