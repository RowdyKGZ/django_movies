# Generated by Django 3.1.5 on 2021-02-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Черновик'),
        ),
    ]
