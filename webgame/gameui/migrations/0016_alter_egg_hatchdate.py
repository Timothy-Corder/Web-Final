# Generated by Django 5.1.3 on 2024-11-22 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameui', '0015_alter_egg_hatchdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egg',
            name='hatchDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 25, 21, 29, 21, 553529)),
        ),
    ]
