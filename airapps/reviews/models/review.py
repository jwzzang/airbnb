from django.db import models
from airapps.common.models import TimeStampedModel


class Review(TimeStampedModel):
    user = models.ForeignKey(
        "users.User",
        verbose_name="유저",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    room = models.ForeignKey(
        "rooms.Room",
        verbose_name="숙소",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        verbose_name="체험",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    payload = models.TextField(
        verbose_name="리뷰 작성",
    )
    rating = models.PositiveIntegerField(
        verbose_name="평점"
    )

    def __str__(self):
        return f"{self.user} / {self.rating}✭"

    class Meta:
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰 관리"
