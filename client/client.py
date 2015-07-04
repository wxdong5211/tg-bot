__author__ = 'Invalid'
import requests

host = 'https://api.telegram.org'


class TgClient:
    """Telegram Client"""

    def __init__(self):
        self.token = None

    def init(self, token):
        self.token = token
        pass

    def update(self, offset=None):
        data = {}
        if offset is not None:
            data.offset = offset
        return requests.post(
            url=host + '/bot' + self.token + "/getUpdates",
            data=data
        ).json()

    def send_msg(self, chat_id, text,
                 message_id=None):
        data = {'chat_id': chat_id, 'text': text}
        if message_id is not None:
            data.reply_to_message_id = message_id
        return requests.post(
            url=host + '/bot' + self.token + "/sendMessage",
            data=data
        ).json()

    def send_photo(self, chat_id, photo,
                   message_id=None):
        data = {'chat_id': chat_id}
        if message_id is not None:
            data.reply_to_message_id = message_id
        return requests.post(
            url=host + '/bot' + self.token + "/sendPhoto",
            data=data,
            files={'photo': photo}
        ).json()


client = TgClient()


def init(token):
    client.init(token)
    pass


def update(offset=None):
    return client.update(offset)


def send_msg(chat_id, text, **kwargs):
    return client.send_msg(chat_id, text, **kwargs)


def send_photo(chat_id, photo, **kwargs):
    return client.send_photo(chat_id, photo, **kwargs)
