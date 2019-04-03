# Generated by Django 2.1.7 on 2019-03-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customapp', '0013_delete_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=50)),
                ('sub', models.CharField(max_length=30)),
            ],
        ),
    ]