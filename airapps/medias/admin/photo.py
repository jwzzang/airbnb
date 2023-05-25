from django.contrib import admin
from airapps.medias.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
