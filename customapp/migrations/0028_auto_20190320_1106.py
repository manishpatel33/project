# Generated by Django 2.1.7 on 2019-03-20 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customapp', '0027_usercomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='usercomment',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='referenced_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]