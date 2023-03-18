from django.contrib import admin
from .models import *

# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ['user_id']


admin.site.register(Chat)
admin.site.register(GroupChat)
admin.site.register(ListGroup, ChatAdmin)
admin.site.register(ListMsg)