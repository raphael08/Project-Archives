# Generated by Django 3.2 on 2023-02-21 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0022_auto_20230221_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='comments',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='progress',
            name='prog',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
