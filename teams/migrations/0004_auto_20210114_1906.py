# Generated by Django 3.1.5 on 2021-01-14 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20210114_1905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['-created']},
        ),
    ]