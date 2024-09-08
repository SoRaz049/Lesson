import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import csv

cred = credentials.Certificate("D:/Data Science/practice files/ML/Trying/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://faceattendance-3e3b7-default-rtdb.firebaseio.com/"})

ref = db.reference("Students")


# data = {
#     'IMG_1390':
#     {
#         "name": "Swaraj Barnwal",
#         "major": "CSIT",
#         "starting_attendance": 2019,
#         "total_attendance": 6,
#         "standing": "G",
#         "year": 4,
#         "last_attendance_time": "2022-12-11 00:54:34"
#     },
#     '321654':
#     {
#         "name": "SRandom",
#         "major": "IT",
#         "starting_attendance": 2013,
#         "total_attendance": 16,
#         "standing": "H",
#         "year": 4,
#         "last_attendance_time": "2022-12-11 00:54:34"
#     },
#     '852741':
#     {
#         "name": "OkRnandom",
#         "major": "CS",
#         "starting_attendance": 2019,
#         "total_attendance": 6,
#         "standing": "G",
#         "year": 4,
#         "last_attendance_time": "2022-12-11 00:54:34"
#     },
#     '963852':
#     {
#         "name": "Swaraj",
#         "major": "CSIT",
#         "starting_attendance": 2019,
#         "total_attendance": 6,
#         "standing": "G",
#         "year": 4,
#         "last_attendance_time": "2022-12-11 00:54:34"
#     }
# }

# for key, value in data.items():
#     ref.child(key).set(value)


with open('D:/Data Science/practice files/ML/Trying/students.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Use student ID as the key
        student_id = row['id']
        # Insert each student's data into Firebase
        ref.child(student_id).set({
            "name": row['name'],
            "major": row['major'],
            "starting_attendance": int(row['starting_attendance']),
            "total_attendance": int(row['total_attendance']),
            "standing": row['standing'],
            "year": int(row['year']),
            "last_attendance_time": row['last_attendance_time']
        })