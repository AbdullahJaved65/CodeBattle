# Generated by Django 4.1.7 on 2023-04-26 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_events_submission'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]
