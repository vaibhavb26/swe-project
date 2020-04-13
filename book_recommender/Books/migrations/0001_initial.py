# Generated by Django 3.0.5 on 2020-04-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=1000)),
                ('book_publisher', models.CharField(max_length=1000)),
                ('book_description', models.TextField()),
                ('published_at', models.TextField()),
                ('book_cover', models.TextField(max_length=1000)),
                ('book_author', models.CharField(max_length=100)),
                ('book_genre', models.ManyToManyField(to='Books.Genre')),
            ],
        ),
    ]
