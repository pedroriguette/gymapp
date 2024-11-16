from django.contrib import admin
from . import models


class TrainingSheetAdmin(admin.ModelAdmin):
    list_display = ["id", "student", "coach", "exercice", "created_at", "updated_at",]
    list_display_links = ["id", "student"]
    search_fields = ["id", "student__full_name",]
    list_display_links = ["id", "student",]
    list_filter = ["id", "student", "coach",]
    ordering = ["id"]
    list_per_page = 50


class GroupAdmin(admin.ModelAdmin):
    list_display = ["name",]


admin.site.register(models.TrainingSheet, TrainingSheetAdmin)
admin.site.register(models.Group, GroupAdmin)
