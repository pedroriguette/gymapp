from django.contrib import admin
from muscle_groups.models import MuscleGroups


@admin.register(MuscleGroups)
class MuscleGroupsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ["name"]
    search_fields = ('name',)
