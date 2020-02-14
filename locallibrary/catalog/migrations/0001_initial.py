# Generated by Django 3.0 on 2020-02-14 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description os the book', max_length=1000)),
                ('isbn', models.CharField(help_text='13 Character ISBN number. International Standard Book Number.', max_length=13, verbose_name='ISBN')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Neurologist', 'Neurologist'), ('Pediatrics', 'Pediatrics'), ('Surgeon', 'Surgeon'), ('Physician', 'Physician'), ('Gaenocologist', 'Gaenocologist'), ('Dermatologist', 'Dermatologist'), ('Dentist', 'Dentist')], default='Physician', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200)),
                ('type', models.CharField(choices=[('inf', 'Infectious'), ('def', 'Deficiency'), ('her', 'Hereditary'), ('phy', 'Physiological'), ('non', 'None'), ('ud', 'Under Diagnosis')], default='non', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(default=None, max_length=200)),
                ('last_Name', models.CharField(default=None, max_length=200)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('t', 'Transgender')], default='m', max_length=20)),
                ('license_Number', models.CharField(default=None, max_length=25, unique=True)),
                ('department', models.ManyToManyField(default=None, to='catalog.Department')),
            ],
            options={
                'ordering': ['first_Name', 'last_Name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre (e.g Science Fiction)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)", max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=13)),
                ('email_id', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('first_Name', models.CharField(default=None, max_length=200)),
                ('last_Name', models.CharField(default=None, max_length=200)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('t', 'Transgender')], default='m', max_length=20)),
                ('birth_Date', models.DateField()),
                ('aadhar_ID', models.CharField(default=None, max_length=12, primary_key=True, serialize=False)),
                ('phone_Number', models.CharField(default=None, max_length=12, unique=True)),
                ('short_Detail_of_Problem', models.CharField(default=True, max_length=500)),
                ('slug_for_Detail', models.SlugField(default=None, max_length=200, unique=True)),
                ('disease_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Disease')),
                ('treatment_Under', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Doctor')),
            ],
            options={
                'ordering': ['first_Name', 'last_Name'],
            },
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this Book across whole Library', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On Loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Book Availability', max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Book')),
                ('borrower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['due_back'],
                'permissions': (('can_mark_returned', 'Set book as returned'),),
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this Boook', to='catalog.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
    ]
