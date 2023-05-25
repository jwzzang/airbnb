from django.contrib import admin
from airapps.direct_messages.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "user",
        "room",
        "created_at",
    )
    list_filter = (
        "created_at",
    )
