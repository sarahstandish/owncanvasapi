# create a single course not read from a file

from canvasapi import Canvas;
from datetime import datetime;
from main import API_KEY, API_URL, TEST_API_KEY, TEST_URL, connect_to_canvas

canvas, account, main_user, courses = connect_to_canvas(TEST_URL, TEST_API_KEY)

# course variables
# see Canvas API documentation for more course options:
# https://canvas.instructure.com/doc/api/courses.html

name = "New course test via Canvas Python library"
course_code = "New S21"
start_date = datetime(2021, 2, 7, 0, 1)
end_date = datetime(2021, 6, 20, 11, 59)
public_description = "A test course created via the Python CanvasAPI library"

course = {
    "name": name,
    "course_code": course_code,
    "start_at": start_date,
    "end_at": end_date,
    "license": "private",
    "is_public": False,
    "public_description": public_description,
    "self_enrollment": True,
    "restrict_enrollments_to_course_dates": False,
    "hide_final_grades": False,
    "time_zone": "America/Los_Angeles",
    "default_view": "modules",
    "course_format": "online",
}

account.create_course(course=course, enroll_me = True)

