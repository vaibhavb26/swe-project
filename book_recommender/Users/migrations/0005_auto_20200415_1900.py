# Generated by Django 3.0.5 on 2020-04-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_bookshelf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookshelf',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]
