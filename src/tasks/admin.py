from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Tasks)
admin.site.register(TaskStatus)
admin.site.register(TaskVisitors)
admin.site.register(Events)
