# Generated by Django 4.2.1 on 2023-06-04 22:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pools', '0005_poolusers_pool_players'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PoolUsers',
            new_name='PoolUser',
        ),
    ]
