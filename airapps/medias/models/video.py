from django.db import models
from airapps.common.models import TimeStampedModel


class Video(TimeStampedModel):
    file = models.FileField(
        verbose_name="동영상",
    )
    experience = models.OneToOneField(
        "experiences.Experience",
        verbose_name="체험",
        on_delete=models.CASCADE,
        related_name="videos",
    )

    def __str__(self):
        return "Video File"

    class Meta:
        verbose_name = "동영상"
        verbose_name_plural = "동영상 관리"
