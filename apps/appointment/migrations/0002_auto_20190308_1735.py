# Generated by Django 2.1.7 on 2019-03-08 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointment', '0001_initial'),
        ('user_profile', '0001_initial'),
        ('hospital', '0002_hospital'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayschedule',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.Doctor'),
        ),
        migrations.AddField(
            model_name='dayschedule',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital'),
        ),
    ]