# Generated by Django 4.1.7 on 2023-03-27 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ai4bharat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sentence',
            old_name='project_id',
            new_name='project',
        ),
    ]