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
                print('credentials not set')

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
    payload = {'studentID': credentials, 'courseName': course}
    r = requests.get('http://162.243.3.45/EnrollMeAPI/api/public/v1/usercourses', params=payload)
    userCourse = r.text

    r = requests.delete('http://162.243.3.45/EnrollMeAPI/api/public/v1/usercourses/' + userCourse)
    if(r.status_code == 404):
        message = r.json()
        message = message['message']
        return message
    if(r.status_code == 204):
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

def schedule():
    payload = {'studentID': credentials}
    r = requests.get('http://162.243.3.45/EnrollMeAPI/api/public/v1/usercourses', params=payload)
    userCourses = r.json()['data']

    print('COURSE\t\t' + 'SECTION\t' + 'PERIOD\t' + 'TIME\t\t\t' + 'PROFESSOR')
    for course in userCourses:
        r = requests.get('http://162.243.3.45/EnrollMeAPI/api/public/v1/courses/' + course['courseID'])
        obj = r.json()['data']
        print(obj['courseID'] + '\t' + obj['section'] + '\t' + obj['period'] + '\t' + obj['startTime'] + '-' + obj['endTime'] + '\t' + obj['professor'])
