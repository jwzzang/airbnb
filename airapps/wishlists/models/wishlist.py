from django.db import models
from airapps.common.models import TimeStampedModel


class Wishlist(TimeStampedModel):
    name = models.CharField(
        verbose_name="목록",
        max_length=150,
    )
    rooms = models.ManyToManyField(
        "rooms.Room",
        verbose_name="숙소",
        related_name="wishlists",
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        verbose_name="체험",
        related_name="wishlists",
    )
    user = models.ForeignKey(
        "users.User",
        verbose_name="주인",
        on_delete=models.CASCADE,
        related_name="wishlists",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "찜 목록"
        verbose_name_plural = "찜 목록 관리"
