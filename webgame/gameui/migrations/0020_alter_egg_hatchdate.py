# Generated by Django 5.1.3 on 2024-11-29 14:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameui', '0019_alter_egg_hatchdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egg',
            name='hatchDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 2, 16, 59, 20, 855981)),
        ),
    ]