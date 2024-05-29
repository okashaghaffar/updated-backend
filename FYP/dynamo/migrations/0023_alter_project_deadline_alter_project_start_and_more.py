# Generated by Django 5.0.3 on 2024-05-26 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamo', '0022_remove_task_assigned_by_alter_project_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2024, 5, 26, 17, 31, 15, 140362)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 26, 17, 31, 15, 140362)),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]