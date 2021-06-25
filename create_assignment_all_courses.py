# create an assignment in all courses
# this is useful for distributing surveys or asking students to upload a photo of themselves

from canvasapi import Canvas;
from canvasapi.exceptions import CanvasException
import csv;
from main import API_KEY, API_URL, TEST_API_KEY, TEST_URL, connect_to_canvas

canvas, account, main_user, courses = connect_to_canvas(TEST_URL, TEST_API_KEY)

# assignment variables
# see assignments documentation https://canvas.instructure.com/doc/api/assignments.html#method.assignments_api.create for more options

assignment_name = 'Study Abroad Survey'

#embed code for google survey or other description or directions for assignment
assignment_description = '<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSfZTky3rv_vH1Bm6aZpEdzEQ7iW8WFtHbTsjqVpmNaPKr441Q/viewform?embedded=true" width="640" height="3678" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>'

assignment_due_at = '2020-11-29T23:59:00'
assignment_lock_at = '2020-11-30T23:59:00' #assignment will be unavailable after lock date

for course in courses:
    try:
        tempCourse = canvas.get_course(course.id)
        #if (not "Leadership" in tempCourse.name):
        tempCourse.create_assignment(
            assignment = {
                'name': assignment_name,
                'description': assignment_description,
                'submission_types': 'external_tool', # if Google form survey
                'notify_of_update': 'true',
                'grading_type': 'not_graded',
                'due_at': assignment_due_at,
                'lock_at': assignment_lock_at,
                'omit_from_final_grade': 'true', # if non-language assignment
                'published': 'true', # if it should be available immediately
            }
        )
        print("Assignment created in " + course.name)
    except CanvasException as e:
        print(str(e) + " in course " + course.name)
