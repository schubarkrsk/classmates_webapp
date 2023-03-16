from django.db import models


# Create your models here.
class Users(models.Model):
    """
    Модель записи расписания задачи
    """
    # Columns
    id = models.IntegerField(primary_key=True)
    familiya = models.CharField(max_length=50, help_text="Фамилия")
    imya = models.CharField(max_length=50, help_text="Имя")
    otchestvo = models.CharField(max_length=50, help_text="Отчество")
    birthday = models.DateField(help_text="День рождения")
    login = models.CharField(max_length=128, help_text="Логин")
    password = models.CharField(max_length=256, help_text="Пароль")

    class Meta:
        verbose_name = "Users"
        ordering = ["familiya", "imya", "otchestvo"]

    def __str__(self):
        return f"<{self.id}> {self.familiya} | {self.imya} | {self.otchestvo} | {self.birthday} | {self.login} | {self.password}"

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
        return f"<{self.id}> {self.familiya} {self.imya} {self.otchestvo}"


class Lessons(models.Model):
    """
    Модель записи таблицы уроков (справочник, не расписание)
    """
    # Columns
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, help_text="Название предмета")
    room = models.TextField(max_length=100, help_text="Номер аудитории")
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, help_text="ФИО преподавателя")

    class Meta:
        verbose_name = "Lesson"
        ordering = ["title"]

    def __str__(self):
        return f"<{self.id}> {self.title} | {self.room} | {self.teacher}"

class Timetable(models.Model):
    """
    Модель записи расписания
    """
    # Columns
    id = models.IntegerField(primary_key=True)
    day_of_week = models.CharField(max_length=100, help_text="День недели")
    lesson_id = models.ForeignKey(Lessons, on_delete=models.CASCADE, help_text="id урока")
    start = models.TextField(max_length=50, help_text="Начало урока")
    end = models.TextField(max_length=50, help_text="Конец урока")

    class Meta:
        verbose_name = "Timetable"
        ordering = ["title"]

    def __str__(self):
        return f"<{self.id}> {self.day_of_week} | {self.lesson_id} | {self.start} | {self.end}"