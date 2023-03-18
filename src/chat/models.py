from django.db import models
from timetable import models as timetable_model

# Create your models here.
class Chat(models.Model):
    """
    Модель записи задачь
    """
    # Columns
    id = models.AutoField(primary_key=True)
    uuidfrom = models.IntegerField(help_text="Отправитель")
    uuidto = models.IntegerField(help_text="Получатель")
    data = models.DateField(help_text="Дата отправления")
    time = models.TimeField(help_text="Время отправления")
    msg = models.CharField(max_length=100, help_text="Сообщение...")

    class Meta:
        verbose_name = "Chat"

    def __str__(self):
        return f"<{self.id}> {self.id_from} | {self.id_to} | {self.data} | {self.time} | {self.msg}"

class Group(models.Model):
    """
    Модель записи групповых чатов
    """
    # Columns
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, help_text="Название")
    uuid = models.IntegerField(help_text="Добавление участника")


    class Meta:
        verbose_name = "Group"

    def __str__(self):
        return f"<{self.id}> {self.title} | {self.uuid}"

class ListGroup(models.Model):
    """
    Модель списка групповых чатов
    """
    # Columns
    id = models.AutoField(primary_key=True)
    chatlist = models.ForeignKey(Group, on_delete=models.CASCADE, help_text="Список чатов")
    uuid = models.ForeignKey(timetable_model.Users, on_delete=models.CASCADE, help_text="id пользователя")


    class Meta:
        verbose_name = "list group"

    def __str__(self):
        return f"<{self.id}>  {self.chatlist} | {self.user}"

class ListSmg(models.Model):
    """
    Модель списка сообщений
    """
    # Columns
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(timetable_model.Users, on_delete=models.CASCADE, help_text="id пользователя")
    chatfrom = models.ForeignKey(Group, on_delete=models.CASCADE, help_text="Пользователь")
    data = models.DateField(help_text="Дата отправления")
    # time = models.TimeField(help_text="Время отправления")

    class Meta:
        verbose_name = "ListSmg"

    def __str__(self):
        return f"<{self.id}> {self.users} | {self.chatfrom} | {self.data} | {self.time}"

