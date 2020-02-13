# Generated by Django 3.0 on 2020-02-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_remove_doctor_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('card', 'Cardiologist'), ('nuro', 'Neurologist'), ('pedia', 'Pediatrics'), ('surg', 'Surgeon'), ('phy', 'Physician'), ('gaen', 'Gaenocologist'), ('derm', 'Dermatologist'), ('den', 'Dentist')], default=None, max_length=6)),
            ],
        ),
    ]
