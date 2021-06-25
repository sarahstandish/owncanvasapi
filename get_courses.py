# get all courses and write them to a file

from canvasapi import Canvas;
from canvasapi.exceptions import CanvasException
from main import API_KEY, API_URL, TEST_API_KEY, TEST_URL, connect_to_canvas

canvas, account, main_user, courses = connect_to_canvas(TEST_URL, TEST_API_KEY)

# file to write courses to
destination_file = "courses/current_courses.csv"
f = open(destination_file, "a")

for course in courses:
    try:
        f.write("\n" + course.name + "," + str(course.id))
    except CanvasException as e:
        print(e)