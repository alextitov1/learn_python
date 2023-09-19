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
import os
import sys
import logging

import ephem
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

load_dotenv()
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


def greet_user(update, context):  # pylint: disable=unused-argument
    """
    Greets the user.

    This function takes an 'update' object and a 'context' object as arguments,
    and replies to the user with a greeting.

    Returns:
    None
    """
    print("Call /start")
    update.message.reply_text("Hi user!")


def talk_to_me(update, context):  # pylint: disable=unused-argument
    """
    Echoes the user's message back to them.

    This function takes an 'update' object and a 'context' object as arguments,
    extracts the text message from the 'update', prints it to the console, and
    then replies to the user with the same message.

    Parameters:
    - update (telegram.Update): An update object containing information about
      the incoming message.
    - context (telegram.ext.CallbackContext): A context object that can be used
      to store data between function calls, although not used in this function.

    Returns:
    None
    """
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def planet_constellation(update, context):  # pylint: disable=unused-argument
    """
    Reply to user with planet constellation.

    This function takes an 'update' object and a 'context' object as arguments,
    extracts the planet name from the 'update', prints it to the console, and
    then replies to the user with the planet constellation.

    Returns:
    None
    """

    planet_name = update.message.text.split()[1].capitalize()
    logging.info("User: %s", planet_name)

    planet = getattr(ephem, planet_name)
    planet = planet()
    planet.compute()
    constellation = ephem.constellation(planet)

    logging.info("Bot: %s", constellation)
    update.message.reply_text(f"{planet_name} in {constellation[1]}")


def main():
    """
    This is the main function that runs the bot.
    """
    mybot = Updater(os.getenv('BOT_TOKEN'), use_context=True)

    bot_dp = mybot.dispatcher
    bot_dp.add_handler(CommandHandler(command="start", callback=greet_user))
    bot_dp.add_handler(CommandHandler(command="planet",
                                      callback=planet_constellation))
    bot_dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot has started")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
