# - coding: utf-8 -*-
# !/usr/bin/python3
#         version: 1.0.0/29.12.20
#

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import functionsClass


# ------------- [ CONNECT TO VK ] -----------
token = ''  # token group
group_id = ""  # ID group
vk_session = vk_api.VkApi(token=token)  # Обработка access_token

longpoll = VkBotLongPoll(vk_session, group_id)  # Данные для работы в сообществе
vk = vk_session.get_api()  # For api requests


# ----------------[ ENGINE ]-----------------
print("The bot is running")

while True:
    try:
        for event in longpoll.listen():  # listen events
            if event.type == VkBotEventType.MESSAGE_NEW:  # if you received a message
                if event.object.message['peer_id'] == event.object.message['from_id']:
                    """ if the message is from private messages """

                    command = event.obj.message["text"].lower()
                    user_id = event.object.message["from_id"]  # variables with user id and message text
                    """ Calling functions from a class """
                    function = functionsClass.RepliesToMsg(vk, event)
                    function.greeting()

    except Exception as error:
        print(error)
