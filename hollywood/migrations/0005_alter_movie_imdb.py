# Generated by Django 4.1 on 2022-11-25 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hollywood', '0004_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb',
            field=models.FloatField(default=True),
        ),
    ]
