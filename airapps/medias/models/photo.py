from django.db import models
from airapps.common.models import TimeStampedModel


class Photo(TimeStampedModel):
    file = models.ImageField(
        verbose_name="사진",
        upload_to="image/"
    )
    description = models.CharField(
        verbose_name="소개",
        max_length=150,
    )
    room = models.ForeignKey(
        "rooms.Room",
        verbose_name="숙소",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        verbose_name="체험",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self):
        return "Photo File"

    class Meta:
        verbose_name = "사진"
        verbose_name_plural = "사진 관리"
