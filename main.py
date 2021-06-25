from canvasapi import Canvas;
from canvasapi.exceptions import CanvasException, InvalidAccessToken
import sys
from keys_and_ids import API_KEY, TEST_API_KEY, own_account_number, my_user_id, test_course_number

API_URL = "https://canvas.instructure.com/"

TEST_URL = "https://canvas.test.instructure.com/"

def connect_to_canvas(url, key):

    try: 
        canvas = Canvas(url, key)
        account = canvas.get_account(own_account_number)
        sarah = canvas.get_user(my_user_id)
        courses = sarah.get_courses()

    except InvalidAccessToken:
        print("Invalid API key. If using the test environment, remember that the environment including the key resets once per month and the key must be regenerated.")
        sys.exit(1)

    except CanvasException as e:
        print(e)

    return canvas, account, sarah, courses


    




