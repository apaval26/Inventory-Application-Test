# Generated by Django 4.2.3 on 2024-04-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppOneSDG', '0002_admin_equipment_device_serial_number_reservation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservationDate',
            field=models.DateField(verbose_name='Date of reservation'),
        ),
    ]
