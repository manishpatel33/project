# Generated by Django 2.1.7 on 2019-04-01 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customapp', '0034_add_group_member_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_group_member',
            name='Group_comment',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
