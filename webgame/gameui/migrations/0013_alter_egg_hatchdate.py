# Generated by Django 5.1.3 on 2024-11-17 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameui', '0012_alter_egg_gender_determined_at_alter_egg_hatchdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egg',
            name='hatchDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 20, 15, 9, 5, 322597)),
        ),
    ]
