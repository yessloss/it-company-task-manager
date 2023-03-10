# Generated by Django 4.1.5 on 2023-02-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0002_alter_worker_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('1', 'Urgent and important'), ('2', 'Urgent and not important'), ('3', 'Not urgent and important'), ('4', 'Not urgent and not important')], default='4', max_length=255),
        ),
    ]
