# Generated by Django 2.1.7 on 2019-03-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customapp', '0024_twit1'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='requested_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
