# Generated by Django 2.1.7 on 2019-03-05 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customapp', '0002_auto_20190304_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='login',
            name='user',
        ),
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='registration',
        ),
    ]