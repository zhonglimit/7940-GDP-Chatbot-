import pymongo
from telegram.ext import CallbackContext
from telegram import Update
import configparser
import os

# Connect to the  MongoDB Altas
username = os.environ['KEY']
password = os.environ['PASSWORD']
cluster = os.environ['CLUSTER']
uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)
db_chatbot = client["db_chatbot"]
collection = db_chatbot["reviews"]

def mylist(update: Update, context: CallbackContext):
    # Get current user information
    query = update.message
    user_id = query.from_user.id

    # Search for records that match the criteria
    records = collection.find({"user info": user_id})

    # Get the Title of all records
    titles = set(record["Title"] for record in records)

    # Assembling the message to be sent to the user
    message = "Your movie list:\n"
    for title in titles:
        message += f"- {title}\n"

    # Send a message to the user
    context.bot.send_message(chat_id=user_id, text=message)

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

    if existing_doc:
    # If the document already exists, let telegram bot indicate that it already exists
       update.callback_query.answer(text="Document already exists.")
    else:
    # If the document does not exist, the data is written to the database
       collection.insert_one(movie_info_dict)
       update.callback_query.answer(text="❤️Added to favorites!")


