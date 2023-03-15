from django.db import models

# Create your models here.
class Tasks(models.Model):
    """
    Модель записи расписания задачи
    """
    # Columns
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, help_text="Название задачи")
    owner = models.TextField(max_length=100, help_text="Ответственный за задачу")
    status = models.TextField(max_length=50, help_text="Статус задачи")
    description = models.TextField(max_length=100, help_text="Задача")
    deadline = models.TextField(max_length=50, help_text="Дедлайн задачи")

    class Meta:
        verbose_name = "Tasks"
        ordering = ["title"]

    def __str__(self):
        return f"<{self.id}> {self.title} | {self.owner} | {self.status} | {self.description} | {self.deadline}"

class Task_visitors(models.Model):
    """
    Модель записи задачь
    """
    # Columns
    id = models.IntegerField(primary_key=True)
    task = models.CharField(max_length=100, help_text="Название задачи")
    visitor_id = models.TextField(max_length=100, help_text="id ответственного")

    class Meta:
        verbose_name = "Task_visitors"
        ordering = ["title"]

    def __str__(self):
        return f"<{self.id}> {self.task} | {self.visitor_id}"

class Task_status(models.Model):
    """
    Модель записи задачь
    """
    # Columns
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, help_text="Статус задачи")

    class Meta:
        verbose_name = "Task_status"
        ordering = ["title"]

    def __str__(self):
        return f"<{self.id}> {self.title}"