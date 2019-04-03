# Generated by Django 2.1.7 on 2019-03-18 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customapp', '0025_userprofile_requested_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='twit1',
            name='Email',
            field=models.EmailField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twit1',
            name='Name',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='follower_id',
            field=models.IntegerField(default=0),
        ),
    ]
