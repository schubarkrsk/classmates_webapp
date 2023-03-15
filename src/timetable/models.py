from django.db import models


# Create your models here.
class Teachers(models.Model):
    """
    Модель записи таблицы учителей
    """
    # Columns
    id = models.IntegerField(primary_key=True)
    familiya = models.CharField(max_length=50, help_text="Фамилия")
    imya = models.CharField(max_length=50, help_text="Имя")
    otchestvo = models.CharField(max_length=50, help_text="Отчество")

    class Meta:
        verbose_name = "Teacher"
        ordering = ["familiya", "imya", "otchestvo"]

    def __str__(self):
        return f"Teacher {self.id}> {self.familiya} {self.imya} {self.otchestvo}"


class Lessons(models.Model):
    """
    Модель записи таблицы уроков (справочник, не расписание)
    """
    # Columns
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, help_text="Название предмета")
    room = models.TextField(max_length=100, help_text="Номер аудитории")
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE(), help_text="ФИО преподавателя")

    class Meta:
        verbose_name = "Lesson"
        ordering = ["title"]

    def __str__(self):
        return f"Lesson {self.id}> {self.title} | {self.room} | {self.teacher}"
