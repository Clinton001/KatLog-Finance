# Generated by Django 2.2.3 on 2019-09-10 11:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_auto_20190910_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katlog_finance',
            name='Date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]