# Generated by Django 4.1.4 on 2022-12-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_alter_visit_current_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='current_url',
            field=models.CharField(max_length=256),
        ),
    ]