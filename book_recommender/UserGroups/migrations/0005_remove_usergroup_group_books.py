# Generated by Django 3.0.5 on 2020-04-15 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserGroups', '0004_groupshelf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergroup',
            name='group_books',
        ),
    ]