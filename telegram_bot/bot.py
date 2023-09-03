# -*- coding: utf-8 -*-
import logging
import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv()
logging.basicConfig(filename="bot.log", level=logging.INFO)


def greet_user(update, context):
    print("Call /start")
    update.message.reply_text("Hi user!")


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(os.getenv('BOT_TOKEN'), use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler(command="start", callback=greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot has started")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
