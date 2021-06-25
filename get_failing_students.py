# get failing students and store them in a file to contact & warn them

from canvasapi import Canvas;
import csv;
from canvasapi.exceptions import CanvasException
from main import API_KEY, API_URL, TEST_API_KEY, TEST_URL, connect_to_canvas

canvas, account, main_user, courses = connect_to_canvas(TEST_URL, TEST_API_KEY)

# input file: a csv file with the courses you want to retrieve failing enrollments from
# must have a 'course_id' column containing the Canvas course id number
current_course_file = 'courses/current_courses.csv'
current_course_numbers = []

file_to_store_grades = 'grades/failing_students.csv'
f = open(file_to_store_grades, "a")

with open(current_course_file, newline='') as csvfile:
    current_courses = csv.DictReader(csvfile)
    for row in current_courses:
        current_course_numbers.append(row['course_id'])

for course in courses:
    if str(course.id) in current_course_numbers:
        try:
            enrollments = course.get_enrollments(type=['StudentEnrollment'])
            for student in enrollments:
                if (student.grades['current_score'] != None) and (student.grades['current_score'] < 60):
                    f.write("\n" + course.name + "," + student.user['name'].strip().title() + "," + str(student.grades['current_score']) + "," + student.user['login_id'])
                    print(student.user['name'])
        except CanvasException as e:
            print(e)
