# Generated by Django 2.1.7 on 2019-03-26 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20190325_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='time_slot',
        ),
    ]