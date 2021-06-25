# for creating new user accounts
# this is the first step before adding users to a course

from canvasapi import Canvas
from canvasapi.exceptions import CanvasException, BadRequest, InvalidAccessToken, Unauthorized
from datetime import date
import sys
import csv
from main import API_KEY, API_URL, TEST_API_KEY, TEST_URL, get_account

try: 
    #user notification will only be sent when registering for the real api, no test api notifications will be sent
    account = get_account(TEST_URL, TEST_API_KEY)

except InvalidAccessToken:
    print("Invalid API key. If using the test environment, remember that the environment including the key resets once per month and the key must be regenerated.")
    sys.exit(1)

#input file should be a .csv with the following required column headings: email, first_name, last_name
#optional columns: class
user_csv = 'users/korean_pm_summer_2021_take2.csv'
new_users = csv.DictReader(open(user_csv))

destination_file = 'users/test_users.csv'
f = open(destination_file, "a")

for line in new_users:
    
    email = line['email']
    first_name = line['first_name']
    last_name = line['last_name']
    class_name = line['class'] if 'class' in line else "No class specified"

    if not email or not first_name or not last_name:
        if not first_name or not last_name:
            print("User missing name and cannot be created: " + email)
            f.write("\n" + "User not created" + "," + email)
        elif first_name and not email:
            print("User missing email and cannot be created: " + first_name)
            f.write("\n" + "User not created" + "," + first_name)
        elif last_name and not email:
            print("User missing email and cannot be created: " + last_name)
            f.write("\n" + "User not created" + "," + last_name)

    else:
        try:
            new_user = account.create_user(
                pseudonym = {
                    'unique_id': email,
                    'send_confirmation': True,
                    'force_self_registration': True,
                },
                user = {
                    'name': first_name + " " + last_name,
                    'short_name': first_name,
                    'sortable_name': last_name + ", " + first_name,
                    'login_id': email,
                    'terms_of_use': 1 #evaluates to true, for acceptance of terms of use
                }
            )
            # add the user to file of created users

            f.write("\n" + str(new_user.id) + "," + email + "," + first_name + "," + last_name + "," + str(date.today()) + "," + class_name)
            print("New user: " + new_user.name + " ID: " + str(new_user.id))

        except BadRequest:
            f.write("\n" + "User not created" + "," + email + "," + first_name + "," + last_name + "," + str(date.today()) + "," + class_name)
            print("This user email has already been added to Canvas: " + email)
        except CanvasException as e:
            print(e)
