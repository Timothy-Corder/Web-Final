# Generated by Django 5.1.3 on 2024-11-17 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameui', '0009_egg_determined_gender_egg_gender_determined_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egg',
            name='hatchDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 20, 13, 34, 15, 784877)),
        ),
    ]
