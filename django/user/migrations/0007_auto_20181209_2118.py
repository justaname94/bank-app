# Generated by Django 2.1.4 on 2018-12-10 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20181209_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], default=0),
        ),
    ]
