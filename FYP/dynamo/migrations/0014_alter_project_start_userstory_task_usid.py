# Generated by Django 5.0.3 on 2024-05-12 06:09

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamo', '0013_alter_project_start_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 12, 11, 9, 39, 26185)),
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamo.project')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='usid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dynamo.userstory'),
        ),
    ]