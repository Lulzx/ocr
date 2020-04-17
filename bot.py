#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import logging
import pytesseract

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hello! Send me an image to extract text from.')


def help(update, context):
    update.message.reply_text('Simply send to me an image.')


def echo(update, context):
    chat_id = update.message.chat.id
    file_id = update.message.photo[0].file_id
    file_name = file_id + ".png"
    picture = context.bot.get_file(file_id).download('./data/{}'.format(file_name))
    try:
        text = pytesseract.image_to_string('./data/{}'.format(file_name))
        if text == "":
            if update.message.chat.type == "supergroup":
                return # won't show error messages in groups
            else:
                text = "sorry, unable to extract text from your image."
    except:
        text = "sorry, an error has occured while processing your image."
    context.bot.send_message(chat_id=chat_id, text=text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    try:
        TOKEN = sys.argv[1]
    except IndexError:
        TOKEN = os.environ.get("TOKEN")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.photo, echo))
    dp.add_error_handler(error)
    updater.start_polling(clean=True, timeout=99999)
    logger.info("Ready to rock..!")
    updater.idle()


if __name__ == '__main__':
    main()

