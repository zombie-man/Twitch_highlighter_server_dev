# Generated by Django 3.1.1 on 2020-10-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid_url', models.CharField(max_length=128, verbose_name='VideoUrl')),
                ('streamer_name', models.CharField(max_length=32, verbose_name='streamer')),
                ('vid_path', models.CharField(max_length=128, verbose_name='vid_path')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='registered_time')),
            ],
        ),
    ]
