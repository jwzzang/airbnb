from django.contrib import admin
from airapps.medias.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
