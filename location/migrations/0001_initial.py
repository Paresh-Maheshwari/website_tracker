# Generated by Django 4.1.4 on 2022-12-12 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('continent', models.CharField(blank=True, max_length=64, null=True)),
                ('country', models.CharField(blank=True, max_length=64, null=True)),
                ('region', models.CharField(blank=True, max_length=64, null=True)),
                ('region_name', models.CharField(blank=True, max_length=64, null=True)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('district', models.CharField(blank=True, max_length=64, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=64, null=True)),
                ('timezone', models.CharField(blank=True, max_length=64, null=True)),
                ('isp', models.CharField(blank=True, max_length=64, null=True)),
                ('org', models.CharField(blank=True, max_length=64, null=True)),
                ('as_number', models.CharField(blank=True, max_length=64, null=True)),
                ('as_name', models.CharField(blank=True, max_length=64, null=True)),
                ('mobile', models.BooleanField(blank=True, null=True)),
                ('proxy', models.BooleanField(blank=True, null=True)),
                ('hosting', models.BooleanField(blank=True, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=64, null=True)),
                ('map_link', models.CharField(blank=True, max_length=256, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TokenSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, unique=True)),
                ('chat_id', models.CharField(max_length=64)),
                ('token_count', models.IntegerField(default=0)),
                ('link', models.CharField(blank=True, max_length=256, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
