from django.contrib import admin
from coaches.models import Coach


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "full_name",
        "email",
        "birthday",
        "phone_number",
        "specialty",
        "entry",
        "start_job",
        "ends_job",
        "created_at",
        "updated_at",
    ]
    search_fields = ["id", "full_name"]
    list_display_links = ["id", "full_name", "email"]
    ordering = ["id"]
    list_filter = ["id", "full_name", "created_at", "updated_at"]
    list_per_page = 50
