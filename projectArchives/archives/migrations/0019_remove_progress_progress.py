# Generated by Django 3.2 on 2023-02-21 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0018_alter_progress_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progress',
            name='progress',
        ),
    ]
