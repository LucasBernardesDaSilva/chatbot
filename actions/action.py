__author__ = 'galleani'

from api.models import Message, UserTelegram
import requests


class Action:
    def __init__(self, user, output):
        self.data = []
        self.output = output
        self.user = user
        self.text = output['output']['text'][0]

    def falhou(self):
        ultimo_id = Message.objects.latest('id').pk
        message = Message.objects.get(id = ultimo_id)
        message.nao_entendida = True
        message.save()
        return [{'type': 'text', 'text': self.text}]
