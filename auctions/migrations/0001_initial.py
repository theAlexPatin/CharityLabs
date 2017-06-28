# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=250)),
                ('current_amount', models.IntegerField()),
                ('highest_bidder', models.CharField(max_length=55)),
                ('highest_bid', models.IntegerField()),
                ('ending_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_id', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('stripe_id', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=55)),
                ('bidder_id', models.CharField(max_length=55)),
                ('time', models.DateField()),
            ],
        ),
    ]
