from django.db import models
from django.utils import timezone


from .constants import (
    MAX_MESSAGE_LENGTH,
    MAX_USERNAME_LENGTH,
    MAX_CONVERSATION_LENGTH
)


class Conversation(models.Model):
    """Structure of a standard conversation."""
    conversation_name = models.CharField(max_length=MAX_CONVERSATION_LENGTH)
    creation_date = models.DateTimeField(
        'date of creation',
        default=timezone.now)

    def __str__(self):
        return self.conversation_name


class Message(models.Model):
    """Structure of a standard message."""
    message_text = models.CharField(max_length=MAX_MESSAGE_LENGTH)
    send_date = models.DateTimeField('date sent', default=timezone.now)
    author = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        default='Anonimous'
        )
    conversation = models.ForeignKey('Conversation', on_delete=models.CASCADE)

    def __str__(self):
        if len(self.message_text) <= 20:
            return "\n{} // sent {}\n".format(
                self.message_text,
                self.send_date
                )

        return "\n{}... // sent {}\n".format(
            self.message_text[:20],
            self.send_date
            )
