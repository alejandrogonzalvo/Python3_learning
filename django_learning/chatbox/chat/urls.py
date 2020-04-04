from django.urls import path

from .views import ConversationListView


app_name = 'chat'
urlpatterns =[
    path('', ConversationListView.as_view(), name='conversation_list')
]
