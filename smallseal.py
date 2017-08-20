#!/usr/local/bin/python3
# coding=utf-8
import os
import logging
import random
from uuid import uuid4
from telegram.ext import Updater, CommandHandler, InlineQueryHandler, Filters, MessageHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
strip = lambda a: a.lstrip(a.split()[0]).lstrip().rstrip()


def wrapper(*args, **kwargs):
    def w(fn):
        def ww(bot, update):
            logging.info(
                'user: {} command: {}'.format(
                    update.message.from_user.username,
                    update.message.text))
            text = fn(bot, update)
            logging.info('response: {}'.format(text))
            if kwargs.get('reply_to', None):
                kwargs['reply_to'] = update.message.message_id
            bot.sendMessage(
                update.message.chat_id,
                reply_to_message_id=kwargs['reply_to'],
                text=text,
                parse_mode=kwargs.get(
                    'parse_mode',
                    None),
                disable_web_page_preview=kwargs.get(
                    'disable_preview',
                    None))
            return 0
        return ww
    return w


def inline_battery(bot, update):
    query = update.inline_query.query
    results = list()
    logging.info(
        'inline {} from {}'.format(
            'no content'
            if query == '' else query,
            update.inline_query.from_user.username))
    if query == '':
        try:
            results.append(
                InlineQueryResultArticle(
                    id=uuid4(),
                    title='淦tmd小海豹',
                    input_message_content=InputTextMessageContent('小海豹真好啊(ﾟ∀。)')))
            bot.answerInlineQuery(
                update.inline_query.id,
                results=results,
                cache_time=5)
            logging.info('return succ, {}'.format('ok'))
        except Exception as e:
            print(e)
    else:
        q = query
        ret = ''
        c = [' ', '']
        for i in q:
            ret = ret + i + random.choice(c)
        logger.info('return: {}'.format(ret))
        results.append(
            InlineQueryResultArticle(
                id=1,
                title=ret,
                input_message_content=InputTextMessageContent(ret)))
        bot.answerInlineQuery(
            update.inline_query.id,
            results=results,
            cache_time=1)


@wrapper(disable_preview=True, parse_mode=None, reply_to=True)
def test(bot, update):
    return str(update)


def main(token, url, path, cert):
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('test', test))

    dp.add_handler(InlineQueryHandler(inline_battery))

    # updater.start_polling()
    updater.start_webhook(listen="0.0.0.0", port=15000, url_path=path)
    updater.bot.setWebhook("https://{}/{}".format(url, path), open(cert, 'rb'))
    updater.idle()

if __name__ == "__main__":
    t = os.getenv('TG_TOKEN')
    url = os.getenv('TG_URL')
    path = os.getenv('TG_PATH')
    cert = os.getenv('TG_CERT')
    main(t, url, path, cert)
