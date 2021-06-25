# delete an assignment in any course that it appears in
# mainly useful if you accidentally create too many assignments using 'create_assignment_all_courses'

from canvasapi import Canvas;
from canvasapi.exceptions import CanvasException
from main import API_KEY, API_URL, TEST_API_KEY, TEST_URL, connect_to_canvas

canvas, account, main_user, courses = connect_to_canvas(TEST_URL, TEST_API_KEY)

name_of_assignment_to_be_deleted = "Study Abroad Survey"

for course in courses:
    try:
        assignments = course.get_assignments()
        assignmentDictionary = {}
        for assignment in assignments:
            assignmentDictionary[assignment.id] = assignment.name
        for assignment in assignmentDictionary:
            if name_of_assignment_to_be_deleted in assignmentDictionary[assignment]:
                course.get_assignment(assignment).delete()
                print("Assignment deleted in " + course.name)
    except CanvasException as e:
        print(e)





