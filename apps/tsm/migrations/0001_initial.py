# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 06:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dc_algorithm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animation_id', models.CharField(default='None', max_length=25, unique=True)),
                ('name', models.CharField(default='None', max_length=25)),
                ('data_variable', models.CharField(default='None', max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResultType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.CharField(max_length=25, unique=True)),
                ('name', models.CharField(max_length=25)),
                ('data_variable', models.CharField(default='normalized_data', max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ToolInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.CharField(max_length=100)),
                ('image_title', models.CharField(max_length=50)),
                ('image_description', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TsmTask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('execution_start', models.DateTimeField(default=datetime.datetime.now, verbose_name='execution_start')),
                ('execution_end', models.DateTimeField(default=datetime.datetime.now, verbose_name='execution_end')),
                ('area_id', models.CharField(max_length=100)),
                ('time_start', models.DateField(verbose_name='time_start')),
                ('time_end', models.DateField(verbose_name='time_end')),
                ('latitude_min', models.FloatField()),
                ('latitude_max', models.FloatField()),
                ('longitude_min', models.FloatField()),
                ('longitude_max', models.FloatField()),
                ('pixel_drill_task', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
                ('pixel_count', models.IntegerField(default=0)),
                ('clean_pixel_count', models.IntegerField(default=0)),
                ('percentage_clean_pixels', models.FloatField(default=0)),
                ('acquisition_list', models.CharField(default='', max_length=100000)),
                ('clean_pixels_per_acquisition', models.CharField(default='', max_length=100000)),
                ('clean_pixel_percentages_per_acquisition', models.CharField(default='', max_length=100000)),
                ('status', models.CharField(default='', max_length=100)),
                ('message', models.CharField(default='', max_length=100)),
                ('scenes_processed', models.IntegerField(default=0)),
                ('total_scenes', models.IntegerField(default=0)),
                ('result_path', models.CharField(default='', max_length=250)),
                ('clear_observations_path', models.CharField(default='', max_length=250)),
                ('water_percentage_path', models.CharField(default='', max_length=250)),
                ('plot_path', models.CharField(default='', max_length=250)),
                ('animation_path', models.CharField(default='None', max_length=250)),
                ('data_path', models.CharField(default='', max_length=250)),
                ('data_netcdf_path', models.CharField(default='', max_length=250)),
                ('animated_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tsm.AnimationType')),
                ('query_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tsm.ResultType')),
                ('satellite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dc_algorithm.Satellite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('task_id', models.UUIDField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='tsmtask',
            unique_together=set([('satellite', 'area_id', 'time_start', 'time_end', 'latitude_max', 'latitude_min', 'longitude_max', 'longitude_min', 'title', 'description', 'query_type', 'animated_product')]),
        ),
    ]
