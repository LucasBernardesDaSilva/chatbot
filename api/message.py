
from .constants import *
import ibm_watson
from .models import LastUserContext, Message, UserTelegram, intents_cont
from .utils import action
import requests
import ast
import datetime
import pytz


def process(text, user, workspace_watson):
    conversation = ibm_watson.AssistantV1(
        version=VERSION_WATSON,
        iam_apikey=API_KEY,
        url=URL
    )
    last_user_context = LastUserContext.objects.filter(user=user)
    context = None
    if last_user_context:
        last_user_context = last_user_context.get()
        if not last_user_context.updated < pytz.utc.localize(datetime.datetime.now()) - datetime.timedelta(minutes=1):
            context = last_user_context.context
            context = ast.literal_eval(context)

    response = conversation.message(workspace_id=workspace_watson, input={
                                    'text': text}, context=context).get_result()
    output = response.get('output')
    intents = response.get('intents')
    entities = response.get('entities')

    new_context = response.get('context')
    if last_user_context:
        last_user_context.context = new_context
        last_user_context.save()
    else:
        LastUserContext.objects.create(user=user, context=new_context)

    salva_resposta(output)
    salvar_intents(intents, entities)

    action_name = output.get('action')
    if action_name:
        response_action = action(user, response, action_name)
        if response_action:
            for i in response_action:
                if i['type'] == 'text':
                    send_text(i['text'], user.chat_id)
                elif i['type'] == 'image':
                    send_photo(i['image'], user.chat_id)
        else:
            return output.get('text')[0]
    else:
        send_text(output.get('text')[0], user.chat_id)


def send_text(text, chat_id):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN_TELEGRAM)
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)


def send_photo(image, chat_id):
    url = 'https://api.telegram.org/bot{}/sendPhoto'.format(TOKEN_TELEGRAM)
    data = {'chat_id': chat_id}
    files = {'photo': image}
    requests.post(url, files=files, data=data)


def sem_permissao(user):
    text = "Ops, {} você não está autorizado a usar esse Boot, Por favor contate o administrador do sistema".format(
        user.first_name)
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN_TELEGRAM)
    data = {'chat_id': user.chat_id, 'text': text}
    requests.post(url, data=data)


def salva_resposta(output):
    ultimo_id = Message.objects.latest('id').pk
    message = Message.objects.get(id=ultimo_id)
    message.respota = output.get('text')[0]
    message.save()


def send_all(text):
    users = UserTelegram.objects.all()
    for user in users:
        print(user)
        url = 'https://api.telegram.org/bot{}/sendMessage'.format(
            TOKEN_TELEGRAM)
        data = {'chat_id': user.chat_id, 'text': text}
        requests.post(url, data=data)


def salvar_intents(intents, entities):
    intent = intents[0]['intent']
    if entities:
        entity = entities[0]['entity']
    else:
        entity = 'null'

    intent_total = intents_cont.objects.filter(intent=intent, entity=entity)
    if intent_total:
        intent = intent_total.get()
        intent.total = intent.total + 1
        intent.save()
    else:
        intent_total = intents_cont.objects.create(
            intent=intent, entity=entity, total=1)
        intent_total.save()
