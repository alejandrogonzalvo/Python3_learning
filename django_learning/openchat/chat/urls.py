from django.urls import path


from . import views


urlpatterns= [
    path('', views.conversation_list, name='Conversation list'),
]