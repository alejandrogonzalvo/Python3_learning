from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView


from .models import Message, Conversation
from .forms import LoginForm


class ConversationListView(ListView):
    template_name = 'chat/conversation_list.html'
    context_object_name = 'conversation_list'

    def get_queryset(self):
        return Conversation.objects.all()


def message_list(request, conversation):
    messages = Message.objects.filter(conversation=conversation)
    return render(
        request,
        'chat/message_list.html',
        {'messages': messages},
        )


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = LoginForm()
    
    return render(request, 'chat/login.html', {'form': form})
