# Generated by Django 3.2.16 on 2022-10-27 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20221027_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='developers',
            new_name='coworkers',
        ),
    ]
