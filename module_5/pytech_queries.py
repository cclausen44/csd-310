# Christopher Clausen
# 6/14/2022
# Module 5.4 Assignment
# This program is used to query information from a database.

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

# Use the find() method to display all documents in the collection
print("- - DISPLAYING STUDENT DOCUMENTS FROM find() QUERY - -")
docs = db.students.find({})
for doc in docs:
    print(f"Student ID: {doc['student_id']}\nFirst Name: {doc['first_name']}\nLast Name: {doc['last_name']}\n")

# Use the find_one() method to display 1 document
print("- - DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY - -")
student = pytech.find_one({"student_id":"1007"})
print(f"Student ID: {student['student_id']}\nFirst Name: {student['first_name']}\nLast Name: {student['last_name']}")

print("\nEnd of program, press any key to exit...")