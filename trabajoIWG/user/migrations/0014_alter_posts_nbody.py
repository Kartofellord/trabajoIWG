# Generated by Django 4.2.5 on 2023-11-16 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_delete_news_posts_lat_posts_lng_posts_nbody_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='nBody',
            field=models.TextField(),
        ),
    ]