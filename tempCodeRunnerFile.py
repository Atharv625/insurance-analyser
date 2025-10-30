# test_db.py
from pymongo import MongoClient

uri = "mongodb://patilatharv625_db_user:6hxVgwSmcfsT8oeq@ac-xyz-shard-00-00.wxrtorg.mongodb.net:27017,ac-xyz-shard-00-01.wxrtorg.mongodb.net:27017,ac-xyz-shard-00-02.wxrtorg.mongodb.net:27017/?ssl=true&replicaSet=atlas-xyz-shard-0&authSource=admin&retryWrites=true&w=majority"
client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("✅ Connected successfully to MongoDB Atlas!")
except Exception as e:
    print("❌ Connection failed:", e)
