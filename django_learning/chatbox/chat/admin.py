from django.contrib import admin


from .models import Message, Conversation


class MessageAdmin(admin.TabularInline):
    model = Message
    fields = ['message_text', 'author', 'send_date']
    extra = 0


class ConversationAdmin(admin.ModelAdmin):
    fields = ['conversation_name']
    inlines = [MessageAdmin]


admin.site.register(Conversation, ConversationAdmin)
