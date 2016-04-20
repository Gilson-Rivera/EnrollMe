# ------------------------------------------------------------
# EnrollMeTools.py
# ------------------------------------------------------------

# Import Requests module
import requests

credentials = ''
with open('credentials.txt') as f:
    for line in f:
        if 'studentID' in line:
            l = line.split('=')
            if (l[1]):
                credentials = l[1]
            else:
                print 'credentials not set'

def enroll(course, section):
    payload = {'studentID': credentials,'courseID': course, 'section': section}
    r = requests.post('http://162.243.3.45/EnrollMeAPI/api/public/v1/usercourses', params=payload)
    if(r.status_code == 404):
        message = r.json()
        message = message['message']
        return message
    if(r.status_code == 201):
        return 'Successfully enrolled in ' + course.upper() + ' ' + section

def drop(course):
    payload = {'studentID': credentials, 'courseID': course}
    r = requests.delete('http://162.243.3.45/EnrollMeAPI/api/public/v1/usercourses', params=payload)
    if(r.status_code == 404):
        message = r.json()
        message = message['message']
        return message
    else:
        return 'Successfully dropped of ' + course.upper()

def change(course, section):
    payload = {'studentID': credentials, 'courseName': course}
    r = requests.get('http://162.243.3.45/EnrollMeAPI/api/public/v1/usercourses', params=payload)
    userCourse = r.text

    payload = {'section': section}
    r = requests.put('http://162.243.3.45/EnrollMeAPI/api/public/v1/usercourses/' + userCourse, params=payload)
    if(r.status_code == 404):
        message = r.json()
        message = message['message']
        return message
    if(r.status_code == 200):
        return 'Successfully changed to ' + course.upper() + ' ' + section

# Requisites:
#   Course, Professor and Time are optional;
#   check for existence of input variables, and
#   construct request URL accordingly before query.
# def available(course, professor, time):

# Requisites:
#   Query for all courses in schedule, and
#   draw a table accordingly.
# def schedule():
