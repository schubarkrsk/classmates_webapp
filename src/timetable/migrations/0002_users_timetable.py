# Generated by Django 4.1.7 on 2023-03-16 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('familiya', models.CharField(help_text='Фамилия', max_length=50)),
                ('imya', models.CharField(help_text='Имя', max_length=50)),
                ('otchestvo', models.CharField(help_text='Отчество', max_length=50)),
                ('birthday', models.DateField(help_text='День рождения')),
                ('login', models.CharField(help_text='Логин', max_length=128)),
                ('password', models.CharField(help_text='Пароль', max_length=256)),
            ],
            options={
                'verbose_name': 'User',
                'ordering': ['familiya', 'imya', 'otchestvo'],
            },
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('day_of_week', models.CharField(help_text='День недели', max_length=100)),
                ('start', models.TimeField(help_text='Начало урока')),
                ('end', models.TimeField(help_text='Конец урока')),
                ('lesson_id', models.ForeignKey(help_text='id урока', on_delete=django.db.models.deletion.CASCADE, to='timetable.lessons')),
            ],
            options={
                'verbose_name': 'Timetable',
                'ordering': ['day_of_week', 'start', 'end'],
            },
        ),
    ]