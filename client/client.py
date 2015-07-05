__author__ = 'Invalid'
import requests


class TgClient:
    """Telegram Client"""

    def __init__(self):
        self.host = None
        self.token = None
        self.uri = None

    def init(self, host, token):
        self.host = host
        self.token = token
        self.uri = self.host + '/bot' + self.token + "/"
        pass

    def update(self, offset=None):
        data = {}
        if offset is not None:
            data.offset = offset
        return self._send(self.uri + "getUpdates", data)

    def send_msg(self, chat_id, text,
                 message_id=None):
        data = {'chat_id': chat_id, 'text': text}
        if message_id is not None:
            data.reply_to_message_id = message_id
        return self._send(self.uri + "sendMessage", data)

    def send_photo(self, chat_id, photo,
                   message_id=None):
        data = {'chat_id': chat_id}
        if message_id is not None:
            data.reply_to_message_id = message_id
        return self._send(self.uri + "sendPhoto", data, files={'photo': photo})

    @staticmethod
    def _send(uri, data, **kwargs):
        return requests.post(url=uri, data=data, **kwargs).json()


client = TgClient()


def init(host, token):
    client.init(host, token)
    pass


def update(offset=None):
    return client.update(offset)


def send_msg(chat_id, text, **kwargs):
    return client.send_msg(chat_id, text, **kwargs)


def send_photo(chat_id, photo, **kwargs):
    return client.send_photo(chat_id, photo, **kwargs)
