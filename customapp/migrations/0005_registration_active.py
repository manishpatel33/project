# Generated by Django 2.1.7 on 2019-03-06 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customapp', '0004_auto_20190305_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='active',
            field=models.CharField(default='', max_length=1),
            preserve_default=False,
        ),
    ]
