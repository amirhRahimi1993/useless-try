# Generated by Django 2.0.2 on 2018-05-16 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Super_users', '0003_remove_dr_info_adder'),
    ]

    operations = [
        migrations.AddField(
            model_name='dr_info',
            name='adder',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='Super_users.collector'),
        ),
    ]