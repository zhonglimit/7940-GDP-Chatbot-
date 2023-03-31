import pymongo
import logging
import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db_chatbot = client["db_chatbot"]
collection = db_chatbot["reviews"]


# Define the function to handle button clicks
def button_click(update, context) -> None:

    # Extract the callback data and the original JSON data from the context
    query = update.callback_query
    movie_info = query.message.text
    user_id = query.from_user.id
    # Process the data that shown on screen.
    movie_info_list = movie_info.split("\n\n")
    movie_info_dict = {item.split(":")[0]: item.split(":")[1] if len(item.split(":")) > 1 else "" for item in movie_info_list}
    # chat_instance: identify the user
    movie_info_dict.update({"user info": user_id})
  
    # check if the specified document already exists in the database
    existing_doc = collection.find_one({"Title": movie_info_dict["Title"], "user info": movie_info_dict["user info"]})
    logging.info(existing_doc)
    if existing_doc:
    # If the document already exists, let telegram bot indicate that it already exists
       update.callback_query.answer(text="Document already exists.")
    else:
    # If the document does not exist, the data is written to the database
       collection.insert_one(movie_info_dict)
       update.callback_query.answer(text="❤️Added to favorites!")


