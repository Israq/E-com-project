# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-11-27 07:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[(b'billing', b'Billing'), (b'shipping', b'Shipping')], max_length=120)),
                ('address_line_1', models.CharField(max_length=120)),
                ('address_line_2', models.CharField(blank=True, max_length=120, null=True)),
                ('Area', models.CharField(max_length=120)),
                ('Block', models.CharField(max_length=120)),
                ('Road_No', models.CharField(max_length=120)),
                ('House_No', models.CharField(max_length=120)),
                ('Flat_No', models.CharField(max_length=120)),
                ('City', models.CharField(max_length=120)),
                ('Phone', models.CharField(max_length=120)),
                ('Country', models.CharField(default=b'Bangladesh', max_length=120)),
                ('billing_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile')),
            ],
        ),
    ]
