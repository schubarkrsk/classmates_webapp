from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Tasks)
admin.site.register(Task_status)
admin.site.register(Task_visitors)
admin.site.register(Events)