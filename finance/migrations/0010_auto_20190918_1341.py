# Generated by Django 2.2.3 on 2019-09-18 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_auto_20190914_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='katlog_finance',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='katlog_finance',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='katlog_finance',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='MediaLib'),
        ),
    ]
