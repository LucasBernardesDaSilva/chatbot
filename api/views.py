from django.shortcuts import render
import ibm_watson
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import message
from .models import UserTelegram, Message, ListFundamentos, ListAlgoritimos
import json
import logging
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


@csrf_exempt
def event(requests):
    try:
        json_request = json.loads(requests.body)
        chat_id = json_request['message']['chat']['id']
        message_id = json_request['message']['message_id']
        text = json_request['message']['text']
        user = UserTelegram.objects.filter(chat_id=chat_id)
        if user:
            user = user.get()
            if user.grr:
                list_fumd = ListFundamentos.objects.filter(grr=user.grr)
                list_alg = ListAlgoritimos.objects.filter(grr=user.grr)
                if list_alg:
                    workspace_watson = 'c3c48fed-c70f-4ba4-9d51-e4530bf61eeb'
                elif list_fumd:
                    workspace_watson = '7a1a0c8e-c18f-4849-8588-812f5aafe2ab'
                else:
                    user.active = False
                    user.save()
            else:
                workspace_watson = '73002612-9bfb-49ac-a953-33e352ab0eaf'
        else:
            first_name = json_request['message']['chat']['first_name']
            last_name = json_request['message']['chat']['last_name']
            user = UserTelegram.objects.create(
                chat_id=chat_id, first_name=first_name, last_name=last_name)
        Message.objects.create(id=message_id, user=user, text=text)

        if user.active:
            message.process(text, user, workspace_watson)
        else:
            message.sem_permissao(user)
    except Exception as ex:
        logger.error(ex)

    return HttpResponse()


@login_required
def index(request):
    return render(request, 'index.html', {'UserTelegram': UserTelegram.objects.all(), 'name': get_perfil_logado(request)})


@login_required
def exibir(request, user_id):
    user = UserTelegram.objects.get(id=user_id)
    msg = Message.objects.filter(user=user)
    return render(request, 'user.html', {'UserTelegram': user, 'Msg': msg, 'name': get_perfil_logado(request)})


@login_required
def get_perfil_logado(request):
    return request.user.username
