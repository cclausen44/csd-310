# Christopher Clausen
# 6/14/2022
# Module 5.3 Assignment

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
chris = {"student_id": "1007", "first_name": "Chris", "last_name": "Clausen"}
trevor = {"student_id": "1008", "first_name": "Trevor", "last_name": "Bailey"}
taylor = {"student_id": "1009", "first_name": "Taylor", "last_name": "Pallete"}

students = [chris, trevor, taylor]

# Create for loop to insert documents
print("- - INSERT STATEMENTS - -")
for student in students:
    student_id = pytech.insert_one(student).inserted_id
    print(f"Inserted student record {student['first_name']} {student['last_name']} into the students collection with document_id {student_id}")

print("\nEnd of program, press any key to exit...")


