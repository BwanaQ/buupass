# Generated by Django 4.0.2 on 2022-02-16 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buupass', '0004_seat_delete_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='available',
        ),
    ]