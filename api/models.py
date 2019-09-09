from __future__ import unicode_literals
from django.db import models


class UserTelegram(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    chat_id = models.CharField(max_length=100)
    grr = models.CharField(max_length=100, blank=True,)

    def __unicode__(self):
        return(self.first_name)

    def __str__(self):
        return(self.first_name)

    class Meta:
        db_table = 'user_telegram'


class Message(models.Model):
    user = models.ForeignKey(UserTelegram, on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now=True, blank=True, null=True)
    text = models.TextField()
    nao_entendida = models.BooleanField(default=False)
    respota = models.TextField()

    def __unicode__(self):
        return (self.text)

    def __str__(self):
        return(self.text)

    class Meta:
        db_table = 'message'


class LastUserContext(models.Model):
    user = models.OneToOneField(UserTelegram, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    context = models.TextField()

    def __unicode__(self):
        return (self.context)

    def __str__(self):
        return(self.user.first_name)

    class Meta:
        db_table = 'last_user_context'


class Permissoes(models.Model):
    user = models.OneToOneField(UserTelegram, on_delete=models.CASCADE)
    arquitetura = models.BooleanField(default=False)
    algoritimos = models.BooleanField(default=False)

    def __str__(self):
        return(self.user.first_name)

    class Meta:
        db_table = 'permissoes'

class intents_cont(models.Model):
    intent = models.CharField(max_length=100)
    entity = models.CharField(max_length=100)
    total = models.IntegerField(default=0)

    def __str__(self):
        return(self.intent)

    class Meta:
        db_table = 'intent_cont'



# Create your models here.
