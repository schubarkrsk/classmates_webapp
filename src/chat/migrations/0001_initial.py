# Generated by Django 4.1.7 on 2023-03-16 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('uuidfrom', models.IntegerField(help_text='Отправитель')),
                ('uuidto', models.IntegerField(help_text='Получатель')),
                ('data', models.DateField(help_text='Дата отправления')),
                ('time', models.TimeField(help_text='Время отправления')),
                ('msg', models.CharField(help_text='Сообщение...', max_length=100)),
            ],
            options={
                'verbose_name': 'Chat',
            },
        ),
    ]
