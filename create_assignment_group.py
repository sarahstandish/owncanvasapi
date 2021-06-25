# create weighted assignment groups in specific Canvas courses
# NB: After using, MUST delete default 'Assignments' group from each Canvas course manually or develop a new script to perform this action

from canvasapi import Canvas;
from canvasapi.exceptions import CanvasException, InvalidAccessToken
import sys
import csv
from main import API_KEY, API_URL, TEST_API_KEY, TEST_URL, connect_to_canvas

canvas, account, main_user, courses = connect_to_canvas(TEST_URL, TEST_API_KEY)

# input file: a csv of the courses you want to create the assignment groups in
# must have a column named 'new_course_id' containing the course Canvas id
all_course_csv = 'courses/summer2021newcourses.csv'

all_courses = csv.DictReader(open(all_course_csv))

for line in all_courses:
    try:
        course_id = int(line['new_course_id'])
        course = canvas.get_course(course_id)

        # for summer
        course.create_assignment_group(name = 'Participation and Attendance', position = 1,
                group_weight = 40)
        course.create_assignment_group(name = 'Homework or independent work', position = 2, group_weight = 30)
        course.create_assignment_group(name = 'Assessments', position = 3, group_weight = 30)
    
    except CanvasException as e:
        print(str(e) + " in course " + course.name)

# for after-school program
#     course.create_assignment_group(name = 'Participation and Attendance', position = 1,
#             group_weight = 20.0)
#     course.create_assignment_group(name = 'Homework', position = 2, group_weight = 20.0)
#     course.create_assignment_group(name = 'Assessments', position = 3, group_weight = 40.0)
#     course.create_assignment_group(name = 'Final project or exam', position = 4, group_weight = 20.0)