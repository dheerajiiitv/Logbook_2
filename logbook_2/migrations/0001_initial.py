# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-20 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingDetails',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('today_objective', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StudDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('present', models.BooleanField(verbose_name=False)),
                ('objective', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='studdetails',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logbook_2.Students'),
        ),
    ]
