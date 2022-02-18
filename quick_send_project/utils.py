from pymongo import MongoClient

def get_default_collection():
  connect_string = 'mongodb://localhost' 
  client = MongoClient(connect_string)
  db = client['wallets']
  collection = db["addresses"]
  return collection
