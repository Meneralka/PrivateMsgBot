# -*- coding: utf-8 -*-
#  Version 1.0.0
import keyboards


class Tools(object):
    """" Class with tools for routine functions """

    def __init__(self, vk, event):
        self.event = event
        self.vk = vk
        self.command = event.obj.message['text'].lower()
        self.commandCommon = event.obj.message['text']
        """ variables to simplify work """

    def send(self, text, keyboard=None, attachment=None, push=1):
        self.vk.messages.send(
            peer_id=self.event.obj.message['peer_id'],
            random_id=0,
            message=text,
            keyboard=keyboard,
            attachment=attachment,
            disable_mentos=push,

        )


class RepliesToMsg(Tools):

    def __init__(self, vk, event):
        super().__init__(vk, event)
        self.tools = Tools(vk, event)

    def greeting(self):

        if not self.event.client_info.keyboard:
            s = "&#128204;Если у вас отсутсвуют кнопки:\nПерейдите в диалог через браузерную версию сайта - vk.me/club"
        else:
            s = ''
        self.send(
            "Здравствуй! Это главное меню.\n"
            "Нажми на нужную кнопку, чтобы получить констультацию по интересующему тебя вопросу.\n"
            f"{s}",
            keyboard=keyboards.greeting_keyboard()

        )
