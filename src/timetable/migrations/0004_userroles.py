# Generated by Django 4.1.7 on 2023-03-17 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_alter_lessons_id_alter_teachers_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('isAdmin', models.BooleanField()),
                ('isTeacher', models.BooleanField()),
                ('uuid', models.ForeignKey(help_text='Пользователь', on_delete=django.db.models.deletion.CASCADE, to='timetable.users')),
            ],
            options={
                'verbose_name': 'User role',
                'ordering': ['id'],
            },
        ),
    ]