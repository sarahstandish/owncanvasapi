# for adding users to the second semester of a course who were already enrolled in the first semester

from canvasapi import Canvas
from canvasapi.exceptions import CanvasException, InvalidAccessToken, ResourceDoesNotExist
import sys
import csv
from main import API_KEY, API_URL, TEST_API_KEY, TEST_URL, connect_to_canvas

canvas, account, main_user, courses = connect_to_canvas(TEST_URL, TEST_API_KEY)

# file to upload users from
# users *must* have already been added to Canvas and have a user id
# file parameters: .csv format, column headings are 'User ID', 'Name', 'Course', and 'Course Number'.
# 'Course Number' must be the Canvas course id of their first semester course
user_csv = 'users/own_observers.csv'

# set the role you want users to be added as
# role options: StudentEnrollment, TaEnrollment, TeacherEnrollment, ObserverEnrollment, DesignerEnrollment
role = 'ObserverEnrollment'

# file you want to read course numbers from
# file parameters: .csv format, column headings: are:
#   'old_course_name' which is the name of the 1st semester course
#   'old_course_id' which is the Canvas id of the 1st semester course
#   'new_course_name' which is the name of the corresponding 2nd semester course
#   'new_course_id' which is the Canvas id of the corresponding 2nd semester course
all_course_csv = 'courses/old_and_new_courses.csv'
all_courses = csv.DictReader(open(all_course_csv))

for line in all_courses:
    try:
        old_course_id = int(line['old_course_id'])
        new_course_id = int(line['new_course_id'])
        old_course_name = line['old_course_name']
        new_course_name = line['new_course_name']
    except ValueError:
        print("Old or new course ID is missing for course: " + str(line))

    users = csv.DictReader(open(user_csv))
    for user in users:
        try:
            user_number = int(user['User ID'])
            user_name = user['Name']
            user_course_name = user['Course']
            user_current_course = int(user['Course Number'])
    
            if old_course_id == user_current_course:
                try:
                    course = canvas.get_course(new_course_id)
                    course.enroll_user(user_number, enrollment_type=role)
                    print(user_name + " was previously enrolled in " + old_course_name + " and is now enrolled in " + new_course_name)
                except ResourceDoesNotExist:
                    print("The course number doesn't exist: " + new_course_id + " and the following user could not be added: " + user_name)
                except CanvasException as e:
                    print("Error with user: " + str(user))
                    print(e)

        except ValueError:
            print("ValueError: Student id or course id is missing for student: " + str(user))
        except TypeError:
            print("TypeError: Student id or course id is missing for student: " + str(user))






