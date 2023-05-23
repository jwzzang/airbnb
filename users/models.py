from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = ("won", "Korean Won")
        USD = ("usd", "Dollar")

    name = models.CharField(
        verbose_name="이름",
        max_length=20,
    )
    avatar = models.ImageField(
        verbose_name="프로필 사진",
        upload_to="image/",
        blank=True,
    )
    is_host = models.BooleanField(
        verbose_name="호스트",
        default=False
    )
    gender = models.CharField(
        verbose_name="성별",
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        verbose_name="언어",
        max_length=10,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        verbose_name="화폐",
        max_length=20,
        choices=CurrencyChoices.choices,
    )
