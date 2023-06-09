from django.db import models
from airapps.common.models import TimeStampedModel


class Room(TimeStampedModel):
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(
        verbose_name="방 이름",
        max_length=150,
    )
    country = models.CharField(
        verbose_name="국가",
        max_length=50,
    )
    city = models.CharField(
        verbose_name="도시",
        max_length=100,
    )
    price = models.PositiveIntegerField(
        verbose_name="가격"
    )
    rooms = models.PositiveIntegerField(
        verbose_name="방 개수"
    )
    toilets = models.PositiveIntegerField(
        verbose_name="화장실"
    )
    description = models.TextField(
        verbose_name="소개"
    )
    address = models.CharField(
        verbose_name="주소",
        max_length=200,
    )
    pet_friendly = models.BooleanField(
        verbose_name="애견동반",
        default=True,
    )
    kind = models.CharField(
        verbose_name="방 종류",
        max_length=20,
        choices=RoomKindChoices.choices
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="주인",
        related_name="rooms",
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        verbose_name="어메니티",
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        verbose_name="카테고리",
        related_name="rooms",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    def total_amenities(self):
        return self.amenities.count()

    def rating(room):
        count = room.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            total_rating = 0
            for review in room.reviews.all().values("rating"):
                total_rating += review["rating"]
                return round(total_rating / count, 1)

    class Meta:
        verbose_name = "방"
        verbose_name_plural = "방 관리"


class Amenity(TimeStampedModel):
    name = models.CharField(
        verbose_name="어메니티 이름",
        max_length=150,
    )
    description = models.TextField(
        verbose_name="소개",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "어메니티"
        verbose_name_plural = "어메니티 관리"
