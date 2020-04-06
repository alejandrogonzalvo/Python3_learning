from django.urls import path

from .views import ConversationListView, MessageListView


app_name = 'chat'
urlpatterns = [
    path(
        '',
        ConversationListView.as_view(),
        name='conversation_list'),

    path(
        '<str:conversation>',
        MessageListView.as_view(),
        name='conversation')
]
