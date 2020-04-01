import datetime

from django.db import models
from django.utils import timezone


class Message(models.Model):
    """Structure of a standard message."""
    message_text = models.CharField(max_length=999)
    send_date = models.DateTimeField('date sent')

    def __str__(self):
        if len(self.message_text) <= 20:
            return "\n{} // sent {}\n".format(self.message_text, self.send_date)
        
        return "\n{}... // sent {}\n".format(self.message_text[:20], self.send_date)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.send_date <= now
    was_published_recently.admin_order_field = 'send_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

