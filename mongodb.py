import pymongo
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db_chatbot = client["db_chatbot"]
collection = db_chatbot["reviews"]


# Define the function to handle button clicks
def button_click(update, context) -> None:
    query = update.callback_query
    message = query.message.text
    chat_instance = query.chat_instance.text
    # Insert the message text into the MongoDB collection
    collection.insert_one({"review": message, "chat_instance": chat_instance})

    # Send a confirmation message to the user
    query.answer(text="Review saved to database")

