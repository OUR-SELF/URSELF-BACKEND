# Generated by Django 3.2.6 on 2021-08-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210822_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail_image',
            field=models.ImageField(default='default-img.png', null=True, upload_to='projects_images'),
        ),
    ]