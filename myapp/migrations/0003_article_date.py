# Generated by Django 2.0 on 2020-04-09 17:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200409_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date '),
        ),
    ]
