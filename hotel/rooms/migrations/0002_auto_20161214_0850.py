# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 08:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rooms.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Addres',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='reservation_finish',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='reservation_start',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='telephone',
            old_name='telephone_nr',
            new_name='nr',
        ),
        migrations.AddField(
            model_name='hotel',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.Address'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='photo',
            field=models.ImageField(default='hotel_minimal_erd.png', upload_to=rooms.models.hotel_directory_path),
        ),
        migrations.AddField(
            model_name='profile',
            name='addres',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.Address'),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, default='', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='hotel_minimal_erd.png', upload_to=rooms.models.profile_directory_path),
        ),
        migrations.AddField(
            model_name='profile',
            name='telephone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.Telephone'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.Room'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='photo',
            field=models.ImageField(default='hotel_minimal_erd.png', upload_to=rooms.models.room_directory_path),
        ),
        migrations.AddField(
            model_name='room',
            name='reservations',
            field=models.ManyToManyField(through='rooms.Reservation', to=settings.AUTH_USER_MODEL),
        ),
    ]
