# Generated by Django 4.2.5 on 2023-11-14 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_news_ngeopos'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='lat',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='lng',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
