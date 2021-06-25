# create courses using a csv file as the input

from canvasapi import Canvas;
from datetime import datetime
from canvasapi.exceptions import CanvasException
import csv
from main import API_KEY, API_URL, TEST_API_KEY, TEST_URL, connect_to_canvas

canvas, account, main_user, courses = connect_to_canvas(TEST_URL, TEST_API_KEY)

new_courses_array = []

# see Canvas API documentation for more course options:
# https://canvas.instructure.com/doc/api/courses.html

# start and end date of new courses
start_date = datetime(2021, 6, 28, 0, 1)
end_date = datetime(2021, 7, 16, 11, 59)

# input file: a csv with the courses that need to be created
# must be .csv format and have the following column headings:
# 'name', the name of the course
# 'course_code', a shorthand designation for the course
# 'public_description', a short description of the course
new_course_csv = 'courses/courses_to_create.csv'

# the file to write the courses to after creation
destination_file = 'courses/test_courses.csv'

# set of terms that apply to all new courses being created
generic_terms = {
    "start_at": start_date,
    "end_at": end_date,
    "license": "private",
    "is_public": False,
    "self_enrollment": True,
    "restrict_enrollments_to_course_dates": False,
    "hide_final_grades": False,
    "time_zone": "America/Los_Angeles",
    "default_view": "modules",
    "course_format": "online", 
    "default_view": "modules",
    "apply_assignment_group_weights": True,
    "open_enrollment": True,
}

# open the file and import each line as a dictionary
with open(new_course_csv, newline='') as csvfile:
    # course name, code, and description are stored in a csv file
    courselist = csv.DictReader(csvfile)
    # add the generic terms to each course; store them in the new_courses_array
    for row in courselist:
        course = row
        for key in generic_terms:
            course.update({key: generic_terms[key]})
        new_courses_array.append(course)

f = open(destination_file, "a")

# create a new course for each item in the new courses array
for new_course in new_courses_array:
    try:
        # no matter what, be sure to keep enroll_me = True, otherwise you will not be enrolled in the course and will not have access to it
        c = account.create_course(course=new_course, enroll_me = True)
        f.write("\n" + c.name + "," + str(c.id))
    except CanvasException as e:
        print(e)