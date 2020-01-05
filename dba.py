from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost')
db=client.admin
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
db = client.test_database
collection = db.test_collection
