from pymongo import MongoClient
from pprint import pprint

MONGO_URL = "mongodb://db:27017"
client = MongoClient(MONGO_URL)
db = client.admin
dbs_list = db.command("listDatabases")
pprint(dbs_list)

print("THE End")