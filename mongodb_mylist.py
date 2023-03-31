import pymongo
from telegram.ext import CallbackContext
from telegram import Update

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
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