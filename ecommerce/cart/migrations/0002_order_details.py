# Generated by Django 5.1.1 on 2024-10-22 04:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_items', models.IntegerField()),
                ('address', models.TextField()),
                ('phoneno', models.BigIntegerField()),
                ('pin', models.IntegerField()),
                ('order_id', models.CharField(blank=True, max_length=20)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(default='pending', max_length=20)),
                ('delivery_status', models.CharField(default='pending', max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
