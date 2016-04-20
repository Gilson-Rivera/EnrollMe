# EnrollMe
##### A Programming Language for UPRM's Enrolling System

---

### About
**EnrollMe** is a scripting language designed to help ease the process of
enrollment for UPRM's students. It achieves this by providing a simple and
easy to learn framework where rookies and first-timers can simply *enroll*,
*drop*, *change* courses in their *schedule*.

### Installation
###### Dependencies
* Python 2.7 or higher
* [Requests: HTTP for Humans](http://docs.python-requests.org/en/master/user/install/)

Make sure dependencies are installed; download, clone or fork repo to desired directory.

### Usage
Please supply student ID for login purposes using the credentials.txt file, like this:
```
studentID=802124321
```

Open Terminal or Powershell, navigate to desired directory and run:
```
python EnrollMe.py
```

After entering the EnrollMe shell environment, students can **enroll**, **drop** and **change** courses. They can also see **available** courses and their current **schedule**.
```
enroll [course] [section]
drop [course]
change [course] [section]
available [course] [professor] [time]
schedule
```

After session is finished, users can *quit* to close EnrollMe shell.
```
quit
```

### Team
* Diego Figueroa - Lead Designer
* Jan Vega - Test Developer
* Wigberto Maldonado - Database Manager
* Luis Vera - Test Developer

Made with :heart: by @diegofigs, @janvega1, @elalcalde, @luisvelop
