# Generated by Django 2.2 on 2019-04-15 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0013_appointment_timeslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='timeslot',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointment.TimeSlot'),
        ),
    ]
