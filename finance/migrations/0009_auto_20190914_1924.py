# Generated by Django 2.2.3 on 2019-09-14 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_auto_20190914_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katlog_finance',
            name='Date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
