# Generated by Django 4.1.7 on 2023-02-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_alter_todo_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
