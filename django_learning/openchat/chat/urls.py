from django.urls import path


from . import views

app_name = 'chat'
urlpatterns = [
    path(
        '',
        views.login,
        name="login"
        ),
    path(
        '<username>/conversations',
        views.ConversationListView.as_view(),
        name='conversation_list'
        ),
    path(
        '<conversation>',
        views.message_list,
        name='message_list'
        ),
]
