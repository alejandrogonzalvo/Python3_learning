from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Message, Conversation


class ConversationListView(generic.ListView):
    """
    Represents the visualization of a conversation.
    """

    model = Conversation

    def get_conversation_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class MessageListView(generic.ListView):
    #TO DO