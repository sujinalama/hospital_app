# Generated by Django 2.1.7 on 2019-03-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_bill_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='height',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
