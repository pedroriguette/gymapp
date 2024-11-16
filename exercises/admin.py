from django.contrib import admin
from exercises.models import Exercice


@admin.register(Exercice)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "category",
        "difficulty_level",
        "equipment",
    ]
    list_display_links = ["id", "name"]
    search_fields = ['name',]
    list_filter = ["id", "name",]
    ordering = ["id"]
