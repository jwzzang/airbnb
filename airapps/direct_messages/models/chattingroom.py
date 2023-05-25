from django.db import models
from airapps.common.models import TimeStampedModel


class ChattingRoom(TimeStampedModel):
    users = models.ManyToManyField(
        "users.User",
        verbose_name="유저",
        related_name="chattingrooms",
    )

    def __str__(self):
        return "Chatting Room"

    class Meta:
        verbose_name = "채팅방"
        verbose_name_plural = "채팅방 관리"
