from django.db import models

# Create your models here.
class Chat(models.Model):
    """
    Модель записи задачь
    """
    # Columns
    id = models.IntegerField(primary_key=True)
    id_from = models.IntegerField(primary_key=True, help_text="Отправитель")
    id_to = models.IntegerField(primary_key=True, help_text="Получатель")
    data = models.CharField(max_length=100, help_text="Дата отправления")
    time = models.CharField(max_length=100, help_text="Время отправления")
    msg = models.CharField(max_length=100, help_text="Сообщение...")

    class Meta:
        verbose_name = "Chat"
        ordering = ["title"]

    def __str__(self):
        return f"<{self.id}> {self.id_from} | {self.id_to} | {self.data} | {self.time} | {self.msg}"