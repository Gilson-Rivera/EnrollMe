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
        message = r.json()['message']
        return message
    if(r.status_code == 201):
        return 'Successfully enrolled in ' + course.upper() + ' ' + section

def drop(course):
    payload = {'studentID': credentials, 'courseName': course}
    r = requests.get('http://162.243.3.45/EnrollMeAPI/api/public/v1/usercourses', params=payload)
    if(r.status_code == 404):
        message = r.json()['message']
        return message
    userCourse = r.text

    r = requests.delete('http://162.243.3.45/EnrollMeAPI/api/public/v1/usercourses/' + userCourse)
    if(r.status_code == 404):
        message = r.json()['message']
        return message
    if(r.status_code == 204):
        return 'Successfully dropped of ' + course.upper()

def change(course, section):
    payload = {'studentID': credentials, 'courseName': course}
    r = requests.get('http://162.243.3.45/EnrollMeAPI/api/public/v1/usercourses', params=payload)
    if(r.status_code == 404):
        message = r.json()['message']
        return message
    userCourse = r.text

    payload = {'section': section}
    r = requests.put('http://162.243.3.45/EnrollMeAPI/api/public/v1/usercourses/' + userCourse, params=payload)
    if(r.status_code == 404):
        message = r.json()['message']
        return message
    if(r.status_code == 200):
        return 'Successfully changed to ' + course.upper() + ' ' + section

# Requisites:
#   Course, Professor and Time are optional;
#   check for existence of input variables, and
#   construct request URL accordingly before query.
# def available(course, professor, time):
def available(course, professor, time):
    pay = []
    if(course):
        pay.append("courseID=" + course)
    if(professor):
        pay.append("professor=" + professor)
    if(time):
        pay.append("time=" + time.upper())
    payload = "&".join(pay)


    r = requests.get('http://162.243.3.45/EnrollMeAPI/api/public/v1/courses?' + payload)
    if(r.status_code == 404):
        print('No courses found.')
        return
    availableCourses = r.json()['data']

    print('\n')
    print('COURSE\t\t' + 'SECTION\t' + 'PERIOD\t' + 'TIME\t\t\t' + 'PROFESSOR')
    for course in availableCourses:
        print(course['courseID'] + '\t' + course['section'] + '\t' + course['period'] + '\t' + course['startTime'] + '-' + course['endTime'] + '\t' + course['professor'])
    print('\n')

def schedule():
    payload = {'studentID': credentials}
    r = requests.get('http://162.243.3.45/EnrollMeAPI/api/public/v1/usercourses', params=payload)
    if(r.status_code == 404):
        print("Schedule is empty.")
        return
    userCourses = r.json()['data']

    print('COURSE\t\t' + 'SECTION\t' + 'PERIOD\t' + 'TIME\t\t\t' + 'PROFESSOR')
    for course in userCourses:
        r = requests.get('http://162.243.3.45/EnrollMeAPI/api/public/v1/courses/' + course['courseID'])
        obj = r.json()['data']
        print(obj['courseID'] + '\t' + obj['section'] + '\t' + obj['period'] + '\t' + obj['startTime'] + '-' + obj['endTime'] + '\t' + obj['professor'])
