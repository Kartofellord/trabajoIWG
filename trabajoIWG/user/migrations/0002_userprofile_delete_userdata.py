# Generated by Django 4.2.6 on 2023-10-22 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userClass', models.PositiveIntegerField()),
                ('userType', models.CharField()),
                ('userFirstName', models.CharField(max_length=15, unique=True)),
                ('realLastName', models.CharField()),
                ('userCountry', models.CharField()),
                ('userFollwers', models.PositiveIntegerField()),
                ('userQualy', models.FloatField()),
                ('userBio', models.CharField(max_length=150)),
                ('userId', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='userData',
        ),
    ]
