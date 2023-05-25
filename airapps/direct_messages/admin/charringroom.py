from django.contrib import admin
from airapps.direct_messages.models import ChattingRoom


@admin.register(ChattingRoom)
class ChattingRoomAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
    )
