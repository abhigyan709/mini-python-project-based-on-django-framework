# Generated by Django 2.2.6 on 2019-11-24 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0023_auto_20191124_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(default='', max_length=200)),
                ('option1', models.CharField(default='', max_length=50)),
                ('option2', models.CharField(default='', max_length=50)),
                ('option3', models.CharField(default='', max_length=50)),
                ('option4', models.CharField(default='', max_length=50)),
                ('answer', models.CharField(default='', max_length=50)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Exam')),
            ],
        ),
    ]