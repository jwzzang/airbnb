from django.db import models
from airapps.common.models import TimeStampedModel


class Experience(TimeStampedModel):
    name = models.CharField(
        verbose_name="경험명",
        max_length=200,
    )
    country = models.CharField(
        verbose_name="국가",
        max_length=50,
    )
    city = models.CharField(
        verbose_name="도시",
        max_length=100,
    )
    host = models.ForeignKey(
        "users.User",
        verbose_name="호스트",
        on_delete=models.CASCADE,
        related_name="experiences",
    )
    price = models.PositiveIntegerField(
        verbose_name="가격"
    )
    address = models.CharField(
        verbose_name="주소",
        max_length=200,
    )
    start_time = models.TimeField(
        verbose_name="시작시간",
    )
    end_time = models.TimeField(
        verbose_name="종료시간",
    )
    description = models.TextField(
        verbose_name="소개",
    )
    perks = models.ManyToManyField(
        "experiences.Perk",
        verbose_name="특전",
        related_name="experiences",
    )
    category = models.ForeignKey(
        "categories.Category",
        verbose_name="카테고리",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="experiences",
    )

    def __str__(self):
        return self.name


class Perk(TimeStampedModel):
    name = models.CharField(
        verbose_name="특전",
        max_length=100,
    )
    detail = models.CharField(
        verbose_name="특전종류",
        max_length=250,
        blank=True,
        default="",
    )
    explanation = models.TextField(
        verbose_name="설명",
        blank=True,
        default="",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "체험"
        verbose_name_plural = "체험 관리"
