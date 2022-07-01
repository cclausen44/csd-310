# Christopher Clausen
# 6/21/2022
# Module 6.2 Assignment
# This program updates a document, changing the last name of one.

# import MongoClient
from pymongo import MongoClient
# Create a variable, url, 
url ="mongodb+srv://admin:admin@cluster0.o3uwqap.mongodb.net/?retryWrites=true&w=majority"
# Create a variable named client
client = MongoClient(url)
# Create a variable named db
db = client["pytech"]
# Create a collection
pytech = db["students"]

# Create the documents for each student
chris = {
    "student_id": "1007", 
    "first_name": "Chris", 
    "last_name": "Clausen"
    }
trevor = {
    "student_id": "1008", 
    "first_name": "Trevor", 
    "last_name": "Bailey"
    }
taylor = {
    "student_id": "1009", 
    "first_name": "Taylor", 
    "last_name": "Pallete"
    }

# Use the find() method to display all documents in the collection
print("- - DISPLAYING STUDENT DOCUMENTS FROM find() QUERY - -")
docs = db.students.find({})
for doc in docs:
    print(f"Student ID: {doc['student_id']}\nFirst Name: {doc['first_name']}\nLast Name: {doc['last_name']}\n")

# Use the update method to change the last name of a document.
result = pytech.update_one(
    {"student_id": "1007"}, {"$set": {"last_name": "Bailey"}})

# Use the find_one() method to display 1 document
print("\n- - DISPLAYING UPDATED STUDENT DOCUMENT FROM find_one() QUERY - -")
clausen = pytech.find_one({"student_id": "1007"})
print(f"Student ID: {clausen['student_id']}\nFirst Name: {clausen['first_name']}\nLast Name: {clausen['last_name']}")

print("\n\nEnd of program, press any key to exit...")