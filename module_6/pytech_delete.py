# Christopher Clausen
# 6/21/2022
# Module 6.3 Assignment
# This program inserts a new document into a collection,
#  then deletes that updated document.

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

# Create another document
ambriell = {
    "student_id": "1010",
    "first_name": "Ambriell",
    "last_name": "Hier"
}

students = [ambriell]

print("- - INSERT STATEMENTS - -")
# Use the insert() method to add another document
for student in students:
    student_id = pytech.insert_one(student).inserted_id
    print(f"Inserted student record {student['first_name']} {student['last_name']} into the students collection with document_id {student_id}")

print("\n")

# Display the new list of student documents
print("- - DISPLAYING NEW STUDENT LIST DOC - -")
docs = db.students.find({})
for doc in docs:
    print(f"Student ID: {doc['student_id']}\nFirst Name: {doc['first_name']}\nLast Name: {doc['last_name']}\n")

# Call the delete_one() method to delete latest student document
myQuery ={"student_id": "1010"}
pytech.delete_one(myQuery)

# Display the updated list of student documents
print("- - DELETED STUDENT ID: 1010 - -")
docs = db.students.find({})
for doc in docs:
    print(f"Student ID: {doc['student_id']}\nFirst Name: {doc['first_name']}\nLast Name: {doc['last_name']}\n")

print("\n\nEnd of program, press any key to exit...")