# Generated by Django 3.2.3 on 2021-05-30 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videos',
            old_name='channel_id',
            new_name='channelId',
        ),
        migrations.RenameField(
            model_name='videos',
            old_name='channel_title',
            new_name='channelTitle',
        ),
        migrations.RenameField(
            model_name='videos',
            old_name='publishedDateTime',
            new_name='publishedTime',
        ),
        migrations.RenameField(
            model_name='videos',
            old_name='video_id',
            new_name='videoId',
        ),
    ]
