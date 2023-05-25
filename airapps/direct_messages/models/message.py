from django.db import models
from airapps.common.models import TimeStampedModel


class Message(TimeStampedModel):
    text = models.TextField(
        verbose_name="채팅",
    )
    user = models.ForeignKey(
        "users.User",
        verbose_name="유저",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages",
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        verbose_name="채팅방",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self):
        return f"{self.user} says: {self.text}"

    class Meta:
        verbose_name = "메세지"
        verbose_name_plural = "메세지 관리"
