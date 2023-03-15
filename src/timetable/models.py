from django.db import models


# Create your models here.
class Teachers(models.Model):
    """
    Модель записи таблицы учителей
    """
    # Columns
    id = models.IntegerField(primary_key=True)
    familiya = models.CharField()
    imya = models.CharField()
    otchestvo = models.CharField()

    def __str__(self):
        return f"Teacher {self.id}> {self.familiya} {self.imya} {self.otchestvo}"


class Lessons(models.Model):
    """
    Модель записи таблицы уроков (справочник, не расписание)
    """
    # Columns
    id = models.IntegerField(primary_key=True)
    title = models.CharField()
    room = models.TextField()
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE())

    def __str__(self):
        return f"Lesson {self.id}> {self.title} | {self.room} | {self.teacher}"
