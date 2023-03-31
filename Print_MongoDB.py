import pymongo
from pprint import pprint


# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# pprint(client.list_database_names())
db = client['db_chatbot']

# Create a new collection
collection = db["reviews"]


#Print all content in a collection 
result = collection.find()
for doc in result:
    print(doc)

#pprint(client.list_database_names())
#pprint(db.list_collection_names())