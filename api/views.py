from .constants import *
from django.shortcuts import render
import ibm_watson
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import message
from .models import UserTelegram, Message, Permissoes
import json
import logging
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


@csrf_exempt
def event(requests):
    try:
        json_request = json.loads(requests.body.decode('utf-8'))
        chat_id = json_request['message']['chat']['id']
        message_id = json_request['message']['message_id']
        text = json_request['message']['text']
        user = UserTelegram.objects.filter(chat_id=chat_id)
        if user:
            user = user.get()
            permissao = Permissoes.objects.filter(user=user)
            permissao = permissao.get()
            if permissao.arquitetura:
                workspace_watson = WORKSPACE_ARQUITETURA
            elif permissao.algoritimos:
                workspace_watson = WORKSPACE_ALGORITMOS
            else:
                user.active = False
        else:
            first_name = json_request['message']['chat']['first_name']
            last_name = json_request['message']['chat']['last_name']
            user = UserTelegram.objects.create(
                chat_id=chat_id, first_name=first_name, last_name=last_name)
            Permissoes.objects.create(user=user)

        Message.objects.create(id=message_id, user=user, text=text)

        if user.active:
            message.process(text, user, workspace_watson)
        else:
            message.sem_permissao(user)
    except Exception as ex:
        logger.error(ex)

    return HttpResponse()
