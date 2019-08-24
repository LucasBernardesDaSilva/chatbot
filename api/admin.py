from django.contrib import admin
from .models import UserTelegram, LastUserContext, Message, ListFundamentos, ListAlgoritimos


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

@admin.register(ListFundamentos)
class ListFundamentosAdmin(admin.ModelAdmin):
    list_display = ['grr']
    search_fields = ['grr']

@admin.register(ListAlgoritimos)
class ListAlgoritimosAdmin(admin.ModelAdmin):
    list_display = ['grr']
    search_fields = ['grr']