# Generated by Django 2.2.3 on 2019-09-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20190906_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katlog_finance',
            name='Image',
            field=models.ImageField(default='default.jpg', height_field=500, max_length=1, upload_to='MediaLib', width_field=500),
        ),
    ]
