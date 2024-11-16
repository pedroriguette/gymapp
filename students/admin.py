from django.contrib import admin
from students.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "full_name", "active", "email", "birthday"]
    list_display_links = ["id", "user"]
    list_display_links = ["id", "full_name"]
    search_fields = ["id", "full_name"]
    ordering = ["id"]
    list_filter = ["id", "full_name", "created_at", "updated_at"]
    list_per_page = 50
    ordering = ["created_at"]
