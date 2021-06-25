# get all enrollments of a specific type and write them to a file

from canvasapi import Canvas;
from canvasapi.exceptions import CanvasException
from main import API_KEY, API_URL, TEST_API_KEY, TEST_URL, connect_to_canvas

canvas, account, main_user, courses = connect_to_canvas(TEST_URL, TEST_API_KEY)

# file to write enrollments to
file_to_store_enrollments = 'users/students2020-21.csv'
f = open(file_to_store_enrollments, "a")

# get all enrollments for a specific role
# roles options: teacher, student, observer, ta, designer
# can get users of multiple types if passed in a list
role = 'student'

for course in courses:
    try:
        users = course.get_users(enrollment_type=role)
        for user in users:
            f.write("\n" + course.name + "," + str(course.id) + "," + user.name + "," + str(user.id))
            print(user.name)
    except CanvasException as e:
        print(e)
