# Generated by Django 5.1.3 on 2024-11-18 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameui', '0013_alter_egg_hatchdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egg',
            name='hatchDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 21, 7, 16, 11, 190483)),
        ),
    ]