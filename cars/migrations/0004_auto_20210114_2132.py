# Generated by Django 3.1.5 on 2021-01-14 16:02

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20210114_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 21, 32, 25, 216671)),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=32),
        ),
    ]
