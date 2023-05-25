from django.contrib import admin
from airapps.categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "kind"
    )
    list_filter = (
        "kind",
    )
