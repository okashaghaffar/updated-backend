# Generated by Django 5.0.3 on 2024-05-26 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamo', '0023_alter_project_deadline_alter_project_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2024, 5, 27, 0, 39, 24, 884706)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 27, 0, 39, 24, 884706)),
        ),
    ]
