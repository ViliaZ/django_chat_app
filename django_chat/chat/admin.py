from django.contrib import admin
from .models import Message, Chat


# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    fields = ('text', 'created_at', 'author', 'receiver')
    list_display = ('text', 'created_at', 'receiver', 'author')
    pass

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)