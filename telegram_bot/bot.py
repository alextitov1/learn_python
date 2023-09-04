# -*- coding: utf-8 -*-
"""
Домашнее задание №1

Использование библиотек: ephem

 * Установите модуль ephem
 * Добавьте в бота команду /planet, которая будет принимать на вход
название планеты на английском, например /planet Mars
 * В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
 * При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import os
from dotenv import load_dotenv
import sys
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv()
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


def greet_user(update, context):
    print("Call /start")
    update.message.reply_text("Hi user!")


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def planet_constellation(update, context):
    planet_name = update.message.text.split()[1]
    print(planet_name)
    logging.info(f'User: {planet_name}')
    planet = getattr(ephem, planet_name)
    planet = planet()
    planet.compute()
    constellation = ephem.constellation(planet)
    logging.info(f'Bot: {constellation}')
    update.message.reply_text(f"{planet_name} in {constellation[1]}")


def main():
    mybot = Updater(os.getenv('BOT_TOKEN'), use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler(command="start", callback=greet_user))
    dp.add_handler(CommandHandler(command="planet",
                   callback=planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot has started")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
