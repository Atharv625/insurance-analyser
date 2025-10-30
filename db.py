

from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create or connect to a database
db = client["insurance_analyzer"]

# Create or connect to a collection
collection = db["claim_decisions"]
