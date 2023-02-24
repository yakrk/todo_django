from django.contrib import admin

# Register your models here.
from .models import Todo, Category

class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "todo", "status", "priority", "due_date", "category")
    list_display_links = ("todo",)
    list_filter = ("status", "priority", "category", "due_date")
    list_editable = ("status",)

admin.site.register(Todo, TodoAdmin)
admin.site.register(Category)