## chatbot.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from OMDB import get_movie_info
from mongodb import button_click, mylist
# The messageHandler is used for all message updates
import configparser
import logging
import os

def main():
    # Load your token and create an Updater for your Bot
    # config = configparser.ConfigParser()
    # config.read('config.ini')
    # updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']),
    #                   use_context=True)

    updater = Updater(
        token=(os.environ['ACCESS_TOKEN']),
        use_context=True
        )
    
    dispatcher = updater.dispatcher


    # You can set this logging module, so you will know when and why things do not work as expected
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

    # register a dispatcher to handle message: here we register an echo dispatcher
    dispatcher.add_handler(
        MessageHandler(Filters.text & (~Filters.command), hello))

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("search", search_movie))
    dispatcher.add_handler(CallbackQueryHandler(button_click))
    dispatcher.add_handler(CommandHandler("mylist", mylist))
    # To start the bot:
    updater.start_polling()
    updater.idle()




#  /hello Kevin , it will reply Good day, Kevin!
def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_chat_action('typing')
    update.message.reply_text("Welcome to MovieFy \n")
    update.message.reply_text(
        "Enter the movie name to get its info by using the command: \n" +
        "/search <movie_name>")
    update.message.reply_text(
        "To get your favourite movies by using the command: \n" + "/mylist")


def search_movie(update: Update, context: CallbackContext) -> None:

    try:
        movie_name = context.args[0]
        logging.info(movie_name)
        update.message.reply_chat_action('typing')
        movie_info = get_movie_info(movie_name)
        message_text = ""

        if movie_info:
            rating_string = f"IMDb Rating {movie_info['imdbRating']}\n"
            for rating in movie_info['Ratings']:
                rating_string += f"\t{rating['Source']} rating is {rating['Value']}\n"

            message_text = (
                f"Title:{movie_info['Title']} ({movie_info['Year']})\n\n" +
                f"Plot:\n\t\t{movie_info['Plot']}\n\n" +
                f"Starring:\n{movie_info['Actors']}\n\n" +
                f"Ratings:\n\t{rating_string}")
            
        else:
            message_text = f"Movie '{movie_name}' not found. Check for typos and try again."
    except (IndexError, ValueError, Exception):
        update.message.reply_text(
            'Pleasee to follow the usage: /search <movie_name>')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Favourite', callback_data = 'add')
    ]])


    update.message.reply_text(message_text, reply_markup=keyboard)










if __name__ == '__main__':
    main()
