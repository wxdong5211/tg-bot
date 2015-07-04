# coding=utf-8
import json
import threading
import time

__author__ = 'Invalid'
from client import client

config = json.load(open("conf/config.json"))
client.init(config['key'])

class TgBot(threading.Thread):
    """Telegram bot"""

    def __init__(self):
        super(TgBot, self).__init__()
        self._stop = threading.Event()
        self.offset = None

    def stop(self):
        self._stop.set()
        pass

    def stopped(self):
        return self._stop.isSet()

    def init(self, offset):
        self.offset = offset
        pass

    def run(self):
        while not self.stopped():
            time.sleep(1)
            print "Run"
                # print client.update()
    # client.send_msg(-14559076, '🌚')
    # img = open("F:/baka.jpg", 'rb')
    # client.send_photo(-14559076, img)
        pass


bot = TgBot()
bot.setDaemon(True)

def start():
    bot.start()
    pass

def stop():
    bot.stop()
    pass
