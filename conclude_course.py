# conclude courses at the end of the semester
# this retires them from the front page of classes; students can no longer turn in assignments
# and grades cannot be changed, among other things

from canvasapi import Canvas;
from canvasapi.exceptions import CanvasException    , ResourceDoesNotExist
import csv;
from main import API_KEY, API_URL, TEST_API_KEY, TEST_URL, connect_to_canvas

canvas, account, main_user, courses = connect_to_canvas(TEST_URL, TEST_API_KEY)

# import file: a file containing a list of the courses to conclude
# parameters: must have a column named 'course_id' that contains the Canvas id of the course to conclude
courses_to_conclude_file = 'courses/courses_to_conclude.csv'

# empty list to contain course numbers retrieved from the file
course_numbers_to_conclude = []

with open(courses_to_conclude_file, newline='') as csvfile:
    current_courses = csv.DictReader(csvfile)
    for row in current_courses:
        # add course number to list
        course_numbers_to_conclude.append(row['course_id'])

# loop through all courses and conclude the course if its number is included in the list
for course in courses:
    if str(course.id) in course_numbers_to_conclude:
        try:
            course.conclude()
            print("Course has been concluded: " + course['name'])
        except CanvasException as e:
            print(e)