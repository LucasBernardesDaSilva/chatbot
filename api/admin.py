from django.contrib import admin
from .models import UserTelegram, LastUserContext, Message, Permissoes, intents_cont


@admin.register(UserTelegram)
class UserTelegramAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    search_fields = ['id', 'first_name', 'last_name']


@admin.register(LastUserContext)
class LastUserContextAdmin(admin.ModelAdmin):
    list_display = ['user', 'updated']
    search_fields = ['id', 'user']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'text', 'created_dt']
    search_fields = ['id', 'text', 'user']


@admin.register(Permissoes)
class PermissoesAdmin(admin.ModelAdmin):
    list_display = ['user', 'arquitetura', 'algoritimos']
    search_fields = ['user']


@admin.register(intents_cont)
class intents_contAdmin(admin.ModelAdmin):
    list_display = ['intent', 'total']
