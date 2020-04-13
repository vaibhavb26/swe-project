# Generated by Django 3.0.5 on 2020-04-13 06:01

import UserGroups.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Books', '0003_auto_20200412_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
                ('group_description', models.TextField(blank=True)),
                ('group_pic', models.ImageField(blank=True, null=True, upload_to=UserGroups.models.get_image_path)),
                ('group_books', models.ManyToManyField(blank=True, to='Books.Book')),
                ('group_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group_genre', models.ManyToManyField(blank=True, to='Books.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.CharField(max_length=2000)),
                ('sent_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserGroups.UserGroup')),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
