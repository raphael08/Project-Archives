# Generated by Django 3.2 on 2023-03-11 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0033_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='level',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archives.level'),
        ),
    ]
