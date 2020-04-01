from django.contrib import admin


from .models import Message

class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['message_text']}),
        ('Sent:', {'fields': ['send_date']})
    ]

    list_display = ('message_text', 'send_date', 'was_published_recently')
    list_filter = ['send_date']
    search_fields = ['message_text']


admin.site.register(Message, MessageAdmin)
