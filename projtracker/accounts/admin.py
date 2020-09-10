from django.contrib import admin

from .models import ProjectNames,UserTasks
# Register your models here.

admin.site.register(ProjectNames)
admin.site.register(UserTasks)