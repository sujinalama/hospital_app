# Generated by Django 2.2 on 2019-04-15 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0015_appointment_appointment_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_no',
        ),
    ]
