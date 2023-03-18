from django.db import models
from timetable import models as timetable_model

# TODO: Натан, какая то херня с моделями
"""
Регистрация групповых чатов (GroupChat)
id - AutoField
owner - ForeginKey для timetable_model.Users
title - VarcharField (название чата)

Члены группового чата
id - AutoField
chat - ForeginKey для GroupChat
user_id - ForeginKey для timetable_model.Users

Сообщения в групповом чате
id - AutoField
chat - ForeginKey для GroupChat
user_id - ForeginKey для timetable_model.Users
date - DateField
time - TimeField
message - TextField
"""

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
        return f"<{self.id}> {self.uuidfrom} | {self.uuidto} | {self.data} | {self.time} | {self.msg}"

class GroupChat(models.Model):
    """
    Модель записи групповых чатов
    """
    # Columns
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(timetable_model.Users, on_delete=models.CASCADE, help_text="Пользователь")
    title = models.CharField(max_length=100, help_text="Название")


    class Meta:
        verbose_name = "Group chat"

    def __str__(self):
        return f"<{self.id}> {self.owner} | {self.title}"

class ListGroup(models.Model):
    """
    Модель списка членов групповых чатов
    """
    # Columns
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE, help_text="Групповой чат")
    user_id = models.ForeignKey(timetable_model.Users, on_delete=models.CASCADE, help_text="Пользователь")


    class Meta:
        verbose_name = "list group"

    def __str__(self):
        return f"<{self.id}>  {self.chat} | {self.user_id}"

class ListMsg(models.Model):
    """
    Модель списка сообщений в групповом чате
    """
    # Columns
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE, help_text="Групповой чат")
    user_id = models.ForeignKey(timetable_model.Users, on_delete=models.CASCADE, help_text="Пользователь")
    data = models.DateField(help_text="Дата отправления")
    time = models.TimeField(help_text="Время отправления")
    message = models.TextField(max_length=100, help_text="Сообщение...")

    class Meta:
        verbose_name = "ListSmg"

    def __str__(self):
        return f"<{self.id}> {self.chat} | {self.user_id} | {self.data} | {self.time} | {self.message}"

