# Generated by Django 3.0.7 on 2020-06-14 22:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0007_auto_20200615_0527'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CPEAccount',
            new_name='UserProfile',
        ),
    ]
