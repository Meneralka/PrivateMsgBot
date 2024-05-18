# - coding: utf-8 -*-
# !/usr/bin/python3
#         ||\\  //||  ||\\\\] ||\\    ||  ||\\\\] ||\\\]  ||\\\\||  ||       ||  //  ||\\\\||
#         || \\// ||  ||      || \\   ||  ||      ||  ||  ||    ||  ||       || //   ||    ||
#         ||  \/  ||  ||\\\]  ||  \\  ||  ||\\\]  ||\\\]  ||\\\\||  ||       ||<<    ||\\\\||
#         ||      ||  ||      ||   \\ ||  ||      ||\\    ||    ||  ||       || \\   ||    ||
#         ||      ||  ||\\\]  ||    \\||  ||\\\]  || \\   ||    ||  ||\\\\]  ||  \\  ||    ||
#
#         version: 1.0.0/29.12.20
#
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import functionsClass


# ------------- [ CONNECT TO VK ] -----------
token = "deb38b62e904d6a1fa520467e43314cb25b885448de2634ea0a88bd57fa9121ba5633e461a9b7b29be845"  # token group
group_id = "195885210"  # ID group
vk_session = vk_api.VkApi(token=token)  # Обработка access_token

longpoll = VkBotLongPoll(vk_session, group_id)  # Данные для работы в сообществе
vk = vk_session.get_api()  # For api requests


# ----------------[ ENGINE ]-----------------
admins = [274868427, 553863104, 308137930, 553499842, 278652149, 553069569, 563663518]

print("The bot is running")

while True:
    try:
        for event in longpoll.listen():  # listen events
            if event.type == VkBotEventType.MESSAGE_NEW:  # if you received a message
                if event.object.message['peer_id'] == event.object.message['from_id'] > 0:
                    """ if the message is from private messages """

                    command = event.obj.message["text"].lower()
                    user_id = event.object.message["from_id"]  # variables with user id and message text
                    """ Calling functions from a class """
                    function = functionsClass.RepliesToMsg(vk, event)
                    function.greeting()

    except Exception as error:
        print(error)
