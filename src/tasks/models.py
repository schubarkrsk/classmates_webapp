from django.db import models
from timetable import models as timetable_model
# Create your models here.

class Task_status(models.Model):
    """
    Модель записи задач
    """
    # Columns
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, help_text="Статус задачи")

    class Meta:
        verbose_name = "Task status"
        ordering = ["title"]

    def __str__(self):
        return f"<{self.id}> {self.title}"

class Tasks(models.Model):
    """
    Модель записи расписания задачи
    """
    # Columns
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, help_text="Название задачи")
    owner = models.ForeignKey(timetable_model.Users, on_delete=models.CASCADE, help_text="Ответственный за задачу")
    status = models.ForeignKey(Task_status, on_delete=models.CASCADE, help_text="Статус задачи")
    description = models.TextField(max_length=100, help_text="Задача")
    deadline = models.DateField(help_text="Дедлайн задачи")

    class Meta:
        verbose_name = "Task"
        ordering = ["title"]

    def __str__(self):
        return f"<{self.id}> {self.title} | {self.owner} | {self.status} | {self.description} | {self.deadline}"

class Task_visitors(models.Model):
    """
    Модель записи задач
    """
    # Columns
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=100, help_text="Название задачи")
    visitor_id = models.ForeignKey(timetable_model.Users, on_delete=models.CASCADE, help_text="id ответственного")

    class Meta:
        verbose_name = "Task visitor"
        ordering = ["task"]

    def __str__(self):
        return f"<{self.id}> {self.task} | {self.visitor_id}"

class Events(models.Model):
    """
    Модель записи расписания задачи
    """
    # Columns
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, help_text="Название мероприятия")
    date = models.DateField(help_text="Дата мероприятия")

    class Meta:
        verbose_name = "Events"
        ordering = ["title"]

    def __str__(self):
        return f"<{self.id}> {self.title} | {self.date}"