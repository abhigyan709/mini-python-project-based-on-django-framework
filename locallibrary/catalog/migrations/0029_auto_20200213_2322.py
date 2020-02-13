# Generated by Django 3.0 on 2020-02-13 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_auto_20200213_2052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['first_Name', 'last_Name']},
        ),
        migrations.RemoveField(
            model_name='patient',
            name='aadhar_Number',
        ),
        migrations.AddField(
            model_name='patient',
            name='aadhar_ID',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
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