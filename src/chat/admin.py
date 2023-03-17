from django.contrib import admin
from .models import *

# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ['User']


admin.site.register(Chat)
admin.site.register(Group)
admin.site.register(ListGroup, ChatAdmin)