# Generated by Django 3.2.9 on 2021-11-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_booking', '0002_auto_20211127_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_reference',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='title',
            field=models.CharField(default='Make a Booking', max_length=200, unique=True),
        ),
    ]
