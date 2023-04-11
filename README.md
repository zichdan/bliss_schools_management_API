<!-- # bliss_schools_management_API -->

<!-- Back to Top Navigation Anchor -->
<a name="readme-top"></a>

<!-- Project Shields -->
<div align="center">

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Stargazers][stars-shield]][stars-url]
  [![Issues][issues-shield]][issues-url]
  [![MIT License][license-shield]][license-url]
  [![Twitter][twitter-shield]][twitter-url]
</div>

<!-- Project Name -->
<div align="center">
  <h1>Bliss_schools_management_API</h1>
</div>

<div>
  <p align="center">
    <a href="https://github.com/zichdan/bliss_schools_management_API#readme"><strong>Explore the Documentation »</strong></a>
    <br />
    <a href="https://github.com/zichdan/bliss_schools_management_API/blob/main/image/bliss_schools_management_API.png">View Demo</a>
    ·
    <a href="https://github.com/zichdan/bliss_schools_management_API/issues">Report Bug</a>
    ·
    <a href="https://github.com/zichdan/bliss_schools_management_API/issues">Request Feature</a>
  </p>
</div>

---

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-bliss-schools-management-API">About Bliss Schools Management API</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#knowledge-acquired">Knowledge Acquired</a></li>
    <li><a href="#project-scope">Project Scope</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#Installation-On-Local-Machine">Installation On Local Machine</a></li>
    <li><a href="#sample">Sample</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
  <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

<!-- About the Project -->
## About Bliss Schools Management API

Bliss Schools Management API does the main function of a school and explains how it works. It enables the school to create an admin account. It allows the registration of students and lecturers. Also, the API allows the school admin to create courses and handling the grading system for the student.

CRUD operations can be carried out on the student data and the courses data, with an easy-to-use Swagger UI setup for testing and integration with the front end.

A Student account have limited access to the app, as a student can only change their profile details and view their profile, courses, grades and GPA.

This Student Management API was built with Python's Flask-RESTX by <a href="https://github.com/zichdan">OKORIE DANIEL EZICHI</a> during Backend Engineering third semester exam at <a href="https://altschoolafrica.com/schools/engineering">AltSchool Africa</a>. This was built as my third semester project in <b>AltSchool Africa</b>. 

<p align="right"><a href="#readme-top">back to top</a></p>

### Built With:

![Python][python]
![Flask][flask]
![SQLite][sqlite]

<p align="right"><a href="#readme-top">back to top</a></p>

---
<!-- Lessons from the Project -->
## Knowledge Acquired

Creating this API helped me learn and practice:
* API Development with Python 'Flask Restx Framework'
* Routing
* Database Management
* Error handling using 'Try and Except Block in Python'
* Debugging
* App Security
* User Authentication and Authorization
* Unit Testing using pytest and Insomnia
* Swagger Documentation

<p align="right"><a href="#readme-top">back to top</a></p>

---
<!-- What the API can do -->
## Project Scope

The Student Management API handles the following:
* Admin Registration
* Teacher Registration
* Student Registration
* Getting Student Information and applying the CRUD operation
* Course Creation
* Getting a Course details and using the CRUD operation
* Assigning a teacher to a course
* Adding a Student Score
* Calculating a Student GPA using the 4.0 Grading System.

The future Versions will cover more aspects and features as needed soon.

---

<!-- GETTING STARTED -->
## Usage

To explore and use this API, follow these steps:

1. Open the web app on your browser:  https://zichdan.pythonanywhere.com/

2. Create an admin or student or Teacher account:
   - Click 'staff' to reveal a dropdown menu of the authentication routes, then register an admin account via the '/admin/signup/admin' route. Input your details and input 'admin' in the 'user-type' to create an admin account.
   - Click 'staff' to reveal a dropdown menu of the authentication routes, then register a teacher account via the '/admin/signup/teacher' route. Input your details and input 'teacher' in the 'user-type' to create a teacher account.
   - Click 'students' to reveal a dropdown menu of the authentication routes, then register a student account via the '/students/signup' route. Input your details and input 'student' in the 'user-type' to create a student account.

3. Login via the '/auth/login' route to generate a JWT token. Copy the access token only without the quotation marks

4. Scroll back up to click <b>Authorize</b> at top right. Enter the JWT token in the given format, for example:
   ```
   Bearer eyJhbtestXVCJ9.eyJbmMzd9.this_rQh8_tl2V1iDlsl_wAOMHcing5334
   ```

5. Click <b>Authorize</b> and then <b>Close</b>.

6. Now authorized, you can create, view, update and delete students, courses and grades via the routes in <b>'students'</b> and **'courses'**. You can also see the information about:
    - All students taking a course
    - All courses taken by a student
    - A student's score in percentage (example: 70.0) and student's grade in letters (eg:'A' , 'B' , 'C' , 'D')
    - A student's GPA, calculated using the 4.0 grading system based on all grades from all courses they are taking (example: 3.3)
   
7. Go to the **Course** Namespace and create a new course before adding a student to the course

8. Then go on ahead to perform other operations and test all the routes. <b>_Awesome!_</b>

9. When you're done, click 'Authorize' at top right again to then 'Logout'. Also, head on to the **'/auth/logout'** route to log the user out and revoke the access token.


<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Installing this app on your machine locally -->
## Installation On Local Machine

<div></div>
<ul style="font-size:18px;">
    <li>Clone the repository to your local machine.</li>
    <li>Navigate to the project directory.</li>
    <li>Create a virtual environment and activate it:</li>
    <li>Install the dependencies:</li>
    <li>Run the application:</li>
</ul>

### To clone the repository

```console
git clone https://github.com/zichdan/bliss_schools_management_API.git
```
### Enter working directory

```console
cd bliss_schools_management_API
```
 OR If Renamed 
```console
cd "name of your folder"    
```
### To create a virtual environment called 'env' 

```console
python -m venv env                 
```
### Activating Virtual environments

 For  Unix or MacOS
```console
source env/bin/activate    
```
 For Windows
```console
source env/scripts/activate         
```

<!-- **Note:** Open the requirement.txt file and remove the uwsgi package which is also the last package. It is likely for you to run into an error if you don't remove it because this is the dyno used to run the app on heroku and will not work on your local machine. After doing this, you can go ahead and install the rest with this command.  -->

### To Install Dependencies 

```console
pip install -r requirement.txt
```

### To create your database locally.

```console
flask shell          # press enter
db                   # press enter
User                 # press enter
Admin                # press enter
Student              # press enter
Course               # press enter
StudentCourse        # press enter
Score                # press enter
db.create_all()      # press enter
exit()               # press enter
```

### Finally, To run the application.

```console
python runserver.py
```
---

<!-- Sample Screenshot -->
## Sample

<br />

[![bliss schools management API][bliss-schools-screenshot]]( https://github.com/zichdan/bliss_schools_management_API/blob/main/image/bliss_schools_management_API.png)

<br/>

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- License -->
## License

Distributed under the MIT License. See <a href="https://github.com/zichdan/bliss_schools_management_API/blob/main/LICENSE">LICENSE</a> for more information.

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Contact -->
## Contact

You can contact me with my social media handles:

[LinkedIn](https://www.linkedin.com/in/daniel-ezichi/) | [Twitter](https://twitter.com/Zichdan_) | [Github](https://github.com/zichdan) | Email: zichdan1999@gmail.com

Project Link: [bliss_schools_management_API](https://github.com/zichdan/bliss_schools_management_API)

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Acknowledgements -->
## Acknowledgements

This project was made possible by:

* [AltSchool Africa School of Engineering](https://altschoolafrica.com/schools/engineering)
* [Caleb Emelike](https://github.com/CalebEmelike)

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Markdown Links & Images -->
[contributors-shield]: https://img.shields.io/github/contributors/zichdan/bliss_schools_management_API.svg?style=for-the-badge
[contributors-url]: https://github.com/zichdan/bliss_schools_management_API/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/zichdan/bliss_schools_management_API.svg?style=for-the-badge
[forks-url]: https://github.com/zichdan/bliss_schools_management_API/network/members
[stars-shield]: https://img.shields.io/github/stars/zichdan/bliss_schools_management_API.svg?style=for-the-badge
[stars-url]: https://github.com/zichdan/bliss_schools_management_API/stargazers
[issues-shield]: https://img.shields.io/github/issues/zichdan/bliss_schools_management_API.svg?style=for-the-badge
[issues-url]: https://github.com/zichdan/bliss_schools_management_API/issues
[license-shield]: https://img.shields.io/github/license/zichdan/bliss_schools_management_API.svg?style=for-the-badge
[license-url]: https://github.com/zichdan/bliss_schools_management_API/blob/main/LICENSE
[twitter-shield]: https://img.shields.io/badge/-@Zichdan_-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/Zichdan_
[twitter-url]: https://twitter.com/Zichdan_
[bliss-schools-screenshot]: https://github.com/zichdan/bliss_schools_management_API/blob/main/image/bliss_schools_management_API.png
[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[sqlite]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
