# Generated by Django 5.1.3 on 2024-11-17 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameui', '0007_alter_egg_hatchdate_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egg',
            name='hatchDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 20, 8, 45, 34, 798355)),
        ),
    ]
