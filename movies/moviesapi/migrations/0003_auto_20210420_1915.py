# Generated by Django 3.1.7 on 2021-04-21 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapi', '0002_moviedata_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='category',
            field=models.CharField(default='action', max_length=200),
        ),
    ]