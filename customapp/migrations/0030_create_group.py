# Generated by Django 2.1.7 on 2019-03-29 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customapp', '0029_auto_20190320_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30)),
                ('member_no', models.IntegerField()),
                ('admin_no', models.IntegerField()),
            ],
        ),
    ]
