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

# available(course, professor, time)
# Pre-Requisites:
#    * User must be logged in
#    * course, professor and time are optional
def available(course, professor, time):

# schedule()
# Pre-Requisites:
#    * User must be logged in
def schedule():
