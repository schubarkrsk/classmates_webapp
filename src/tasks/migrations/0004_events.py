# Generated by Django 4.1.7 on 2023-04-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_tasks_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Название мероприятия', max_length=100)),
                ('date', models.DateField(help_text='Дата задачи')),
            ],
            options={
                'verbose_name': 'Events',
                'ordering': ['title'],
            },
        ),
    ]
