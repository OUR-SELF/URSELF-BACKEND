# Generated by Django 3.2.6 on 2021-08-22 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumer_users',
            name='avatar',
        ),
    ]
