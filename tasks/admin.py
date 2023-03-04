from django.contrib import admin
from .models import Taskss

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.

admin.site.register(Taskss, TaskAdmin)

