from django.db import models
from timetable import models as timetablemodel

# Create your models here.
class Chat(models.Model):
    """
    Модель записи задачь
    """
    # Columns
    id = models.IntegerField(primary_key=True)
    id_from = models.ForeignKey(timetablemodel.Users, on_delete=models.CASCADE, help_text="Отправитель")
    id_to = models.ForeignKey(timetablemodel.Users, on_delete=models.CASCADE, help_text="Получатель")
    data = models.DateField(help_text="Дата отправления")
    time = models.TimeField(help_text="Время отправления")
    msg = models.CharField(max_length=100, help_text="Сообщение...")

    class Meta:
        verbose_name = "Chat"

    def __str__(self):
        return f"<{self.id}> {self.id_from} | {self.id_to} | {self.data} | {self.time} | {self.msg}"