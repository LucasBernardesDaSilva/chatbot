__author__ = 'galleani'

from api.models import Message, UserTelegram
import requests


class Action:
    def __init__(self, user, output):
        self.data = []
        self.output = output
        self.user = user
        self.text = output['output']['text'][0]

    def add_grr(self):
        self.user.grr = self.output['context']['number']
        self.user.save()

        return [{'type':'text','text': self.text}]
