# OWN Canvas API
## A collection of Python scripts to manage OneWorld Now! classes on Canvas

This collection makes it easier to perform bulk actions on multiple Canvas courses at once. It makes managing the OneWorld Now! Canvas environment significantly faster. It's built on the [Canvas API Python library](https://canvasapi.readthedocs.io/en/stable/).

## Author
Created by [Sarah Standish](https://github.com/sarahstandish/)

## Features
Included but not limited to:
- Add users to Canvas
- Enroll multiple users in courses in any role (student, teacher, ta, observer)
- Create new Canvas courses
- Set assignment groups
- Download grades
- Download grades of failing students only
- Create assignments and populate them to all courses at once
- Conclude courses

## Installation and use
These scripts can be downloaded and run individually from the command line. Run `pip install canvas API` to install the Canvas API library.

## Useful references
- [Canvas API Python library documentation](https://canvasapi.readthedocs.io)
- [Canvas API Python library Slack](https://ucfopen.slack.com/)
- [Canvas LMS REST API documentation](https://canvas.instructure.com/doc/api/)

## The Canvas test environment
The test environment for any Canvas page can be accessed by inserting 'test' into the URL after 'canvas':
    canvas.instructure.com --> canvas.test.instructure.com
    
Any script in this collection can be run on either the test or real-world environment. It is *highly* recommended to run every script in the test environment first exactly as it will be run in the realtime environment, and then visually examine the test GUI to make sure the result was as intended.

The test environment resets itself automatically once per month.

## Authorization
API keys can be generated from the account --> settings menu in Canvas. When the test environment resets, it will reset the API key as well and a new one will need to be generated.

## Account permissions
In free Canvas accounts, the highest level of permissions is 'teacher'. As the account holder, Sarah holds 'teacher' level permissions for every course. All the scripts in this collection are well within the permissions of the teacher role but attempting to perform other actions normally associated with 'admin' role will generate `Unauthorized` or `Forbidden` exceptions. An example of an `Unauthorized` action is attempting to retrieve users not enrolled in a course Sarah is a 'teacher' of. There is no way around this.

## Sources of help
The [Canvas API Python Slack](https://ucfopen.slack.com/) is a community of genuinely helpful people available to help with troubleshooting.
