# Generated by Django 3.2 on 2023-02-21 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0021_rename_progress_progress_prog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='comments',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='progress',
            name='prog',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
