# Generated by Django 4.1.5 on 2023-01-18 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task_manager.position'),
        ),
    ]
