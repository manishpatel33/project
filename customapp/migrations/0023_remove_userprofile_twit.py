# Generated by Django 2.1.7 on 2019-03-15 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customapp', '0022_auto_20190315_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='twit',
        ),
    ]
