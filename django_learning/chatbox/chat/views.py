from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Message, Conversation


class ConversationListView(generic.ListView):
    """
    Represents the visualization of a conversation.
    """
    template_name = 'templates/chat/conversation_list.html'
    context_object_name = 'conversation_list'

    def get_queryset(self):
        return Conversation.objects.all()


class MessageListView(generic.ListView):
    """
    Represents the visualization of a list of messages from
    a specific conversation.
    """

    model = Message
    template_name = 'templates/chat/message_list.html'
    context_object_name = 'message_list'

    def get_queryset(self):
        return Message.objects.filter(
            conversation=self.kwargs['conversation_id']
            )
