from django.contrib import admin
from airapps.experiences.models import Experience, Perk


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "start_time",
        "end_time",
        "created_at",
    )
    list_filter = (
        "category",
    )


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "detail",
        "explanation",
    )
