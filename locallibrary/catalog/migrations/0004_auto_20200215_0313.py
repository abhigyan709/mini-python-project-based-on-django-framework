# Generated by Django 3.0 on 2020-02-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200215_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='short_Detail_of_Problem',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
