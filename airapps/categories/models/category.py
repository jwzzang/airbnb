from django.db import models
from airapps.common.models import TimeStampedModel


class Category(TimeStampedModel):
    class CategoryKindChoices(models.TextChoices):
        ROOMS = ("rooms", "Rooms")
        EXPERIENCES = ("experiences", "Experiences")

    name = models.CharField(
        verbose_name="카테고리",
        max_length=50,
    )
    kind = models.CharField(
        verbose_name="카테고리 종류",
        max_length=20,
        choices=CategoryKindChoices.choices
    )
