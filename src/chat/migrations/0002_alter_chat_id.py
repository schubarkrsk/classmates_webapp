# Generated by Django 4.1.7 on 2023-03-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
