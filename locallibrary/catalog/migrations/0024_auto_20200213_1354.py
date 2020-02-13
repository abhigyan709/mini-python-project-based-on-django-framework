# Generated by Django 3.0 on 2020-02-13 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_auto_20200213_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='disease_Type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Disease'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='treatment_Under',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Doctor'),
        ),
    ]