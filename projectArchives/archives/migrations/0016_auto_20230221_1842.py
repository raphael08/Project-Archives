# Generated by Django 3.2 on 2023-02-21 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0015_rename_project_progress_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='archives.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='archives.student'),
        ),
    ]
