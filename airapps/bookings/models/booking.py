from django.db import models
from airapps.common.models import TimeStampedModel


class Booking(TimeStampedModel):
    class BookingKindChoices(models.TextChoices):
        ROOM = ("room", "Room")
        EXPERIENCE = ("experience", "Experience")

    kind = models.CharField(
        verbose_name="종류",
        max_length=15,
        choices=BookingKindChoices.choices
    )
    user = models.ForeignKey(
        "users.User",
        verbose_name="주인",
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    room = models.ForeignKey(
        "rooms.Room",
        verbose_name="숙소",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        verbose_name="체험",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings",
    )
    check_in = models.DateField(
        verbose_name="입실",
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        verbose_name="퇴실",
        null=True,
        blank=True,
    )
    experience_time = models.DateTimeField(
        verbose_name="체험 일정",
        null=True,
        blank=True,
    )
    guests = models.PositiveIntegerField(
        verbose_name="인원"
    )

    def __str__(self):
        return f"{self.kind.title()} booking for: {self.user}"

    class Meta:
        verbose_name = "예약"
        verbose_name_plural = "예약 관리"
