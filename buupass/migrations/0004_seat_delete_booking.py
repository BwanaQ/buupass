# Generated by Django 4.0.2 on 2022-02-16 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buupass', '0003_booking_user_bus_available_alter_bus_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buupass.bus')),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
