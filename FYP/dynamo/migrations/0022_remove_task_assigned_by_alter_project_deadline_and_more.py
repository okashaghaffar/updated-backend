# Generated by Django 5.0.3 on 2024-05-26 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamo', '0021_alter_project_deadline_alter_project_start_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_by',
        ),
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2024, 5, 26, 17, 30, 48, 999009)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 26, 17, 30, 48, 999009)),
        ),
    ]