# Generated by Django 4.1.4 on 2022-12-12 19:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0014_dailyvisit_author_monthlyvisit_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyvisit',
            name='today',
            field=models.DateField(default=datetime.date(2022, 12, 13)),
        ),
        migrations.AlterField(
            model_name='monthlyvisit',
            name='month',
            field=models.IntegerField(default=datetime.date(2022, 12, 13)),
        ),
        migrations.AlterField(
            model_name='monthlyvisit',
            name='year',
            field=models.IntegerField(default=datetime.date(2022, 12, 13)),
        ),
        migrations.AlterField(
            model_name='yearlyvisit',
            name='year',
            field=models.IntegerField(default=datetime.date(2022, 12, 13)),
        ),
    ]