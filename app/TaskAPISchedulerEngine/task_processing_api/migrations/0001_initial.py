# Generated by Django 3.1 on 2020-11-16 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True)),
                ('task_type', models.CharField(choices=[('A', 'А'), ('B1', 'Б1'), ('B2', 'Б2')], max_length=2)),
                ('status', models.CharField(choices=[('Created', 'Создана'), ('Executing', 'Выполняется'), ('Executed', 'Выполнена')], default='Created', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='task_processing_api.task')),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
