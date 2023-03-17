from django.contrib import admin
from .models import Teachers, Lessons, Users, UserRoles

# Register your models here.
admin.site.register(Teachers)
admin.site.register(Lessons)
admin.site.register(Users)
admin.site.register(UserRoles)
