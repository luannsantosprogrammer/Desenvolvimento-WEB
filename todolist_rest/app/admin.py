from django.contrib import admin
from app.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','completed','created_at']
    list_filter = ['title','completed','created_at']
admin.site.register(Task, TaskAdmin)
