# Generated by Django 5.0 on 2024-01-03 21:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_id', models.AutoField(primary_key=True, serialize=False)),
                ('board_name', models.CharField(max_length=20)),
                ('dimension', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('tile_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=200)),
                ('num_wins', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BoardTile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BingoBackend.board')),
                ('tile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BingoBackend.tile')),
            ],
        ),
        migrations.CreateModel(
            name='BoardTileUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_row', models.IntegerField()),
                ('position_col', models.IntegerField()),
                ('selected', models.BooleanField(default=False)),
                ('board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BingoBackend.board')),
                ('tile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BingoBackend.tile')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BingoBackend.user')),
            ],
        ),
    ]