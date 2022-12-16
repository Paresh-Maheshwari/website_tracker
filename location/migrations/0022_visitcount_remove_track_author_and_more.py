# Generated by Django 4.1.4 on 2022-12-13 08:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0021_remove_dailyvisit_author_remove_monthlyvisit_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_count', models.IntegerField(default=0)),
                ('today', models.DateField(default=datetime.date(2022, 12, 13))),
                ('today_total', models.IntegerField(default=0)),
                ('monthly_total', models.IntegerField(default=0)),
                ('yearly_total', models.IntegerField(default=0)),
                ('last_visit_date', models.DateField(default=datetime.date(2022, 12, 13))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='track',
            name='author',
        ),
        migrations.RemoveField(
            model_name='track',
            name='daily_visits',
        ),
        migrations.RemoveField(
            model_name='track',
            name='monthly_visits',
        ),
        migrations.RemoveField(
            model_name='track',
            name='yearly_visits',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='author',
        ),
        migrations.DeleteModel(
            name='DailyVisit',
        ),
        migrations.DeleteModel(
            name='MonthlyVisit',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
        migrations.DeleteModel(
            name='Visit',
        ),
        migrations.DeleteModel(
            name='YearlyVisit',
        ),
    ]