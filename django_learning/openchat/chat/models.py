from django.db import models


class conversation(models.Model):
    conversation_name = models.CharField(max_length=30)
