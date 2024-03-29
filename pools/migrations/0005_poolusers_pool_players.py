# Generated by Django 4.2.1 on 2023-06-04 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pools', '0004_userleague'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoolUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pools.pool')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pool',
            name='players',
            field=models.ManyToManyField(related_name='players', through='pools.PoolUsers', to=settings.AUTH_USER_MODEL),
        ),
    ]
