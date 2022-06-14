# Christopher Clausen
# 6/14/2022
# Module 5 Assignment

# import MongoClient
from pymongo import MongoClient

# Create a variable, url, 
url ="mongodb+srv://admin:admin@cluster0.o3uwqap.mongodb.net/?retryWrites=true&w=majority"

# Create a variable named client
client = MongoClient(url)

# Create a variable named db
db=client.pytech

# Print output
print("-- Pytech Collection List --")
print(db.list_collection_names())

print("\nEnd of program, press any key to exit...")