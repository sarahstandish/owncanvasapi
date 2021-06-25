# for adding users not continuing from a previously enrolled course
# such as the at the beginning of semester 1 or new students starting in semester 2
# NB: users must first be created using new_user.py

from canvasapi import Canvas
from canvasapi.exceptions import CanvasException, ResourceDoesNotExist
import csv
from main import API_KEY, API_URL, TEST_API_KEY, TEST_URL, connect_to_canvas

canvas, account, main_user, courses = connect_to_canvas(TEST_URL, TEST_API_KEY)

# file to upload users from
# users *must* have already been added to Canvas and have a user id
# file parameters: .csv format, column headings are 'User ID', 'Name', 'Course', and 'Course Number'.
# 'Course Number' must be the Canvas course id
user_csv = 'users/session1_students_summer_2021.csv'
all_users = csv.DictReader(open(user_csv))

# set the role you want users to be added as
# role options: StudentEnrollment, TaEnrollment, TeacherEnrollment, ObserverEnrollment, DesignerEnrollment
role = 'StudentEnrollment'

for user in all_users:
    user_number = int(user['User ID'])
    user_name = user['Name']
    user_course_name = user['Course']
    course_id = user['Course Number']
    if not user_number or not course_id:
        print("User missing information and could not be created: " + str(user))

    else:
        try:
            course = canvas.get_course(course_id)
            course.enroll_user(user_number, enrollment_type=role)
            print(user_name + " is now enrolled in " + user_course_name)
        except ResourceDoesNotExist:
            print("The course number doesn't exist: " + course_id + " and the following user could not be added: " + user_name)
        except CanvasException as e:
            print(e)
