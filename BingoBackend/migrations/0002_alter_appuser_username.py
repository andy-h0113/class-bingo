# Generated by Django 5.0 on 2024-01-19 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BingoBackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
