# Generated by Django 2.0.2 on 2018-05-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Super_users', '0006_auto_20180520_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dr_info',
            name='Dr_photo_link',
            field=models.FileField(upload_to=''),
        ),
    ]
