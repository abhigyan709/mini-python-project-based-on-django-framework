# Generated by Django 3.0 on 2020-02-13 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_doctor_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='department',
        ),
    ]
