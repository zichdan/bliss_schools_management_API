from ..utils import db
from flask_restx import Namespace, Resource, fields
from ..student_managemanet.serializers import (grade_model_field, grade_update_model_field,student_course_field)
# from .students import student_namespace,student_signup_model,student_model

from ..models.grades import Score
from ..models.users import Student
from ..models.courses import StudentCourse, Course

from ..utils.grades_conversion import get_letter_grade, convert_grade_to_gpa

# from ..utils.decorators import admin_required
from werkzeug.security import generate_password_hash
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity


student_grades_namespace = Namespace('Grade', description='Namespace for Students')


student_course_model = student_grades_namespace.model( 'StudentCourse', student_course_field)

grade_model = student_grades_namespace.model('Grade', grade_model_field)

grade_update_model = student_grades_namespace.model('GradeUpdate', grade_update_model_field)




 

@student_grades_namespace.route('/grades')
class GetAddUpdateGrades(Resource):

        
    @student_grades_namespace.expect(grade_model)
    @student_grades_namespace.doc(
        description = "Upload a Student's Grade in a Course - Admins Only",
        # params = {
        #     'student_id': "The Student's ID"
        # }
    )
    # @admin_required()
    def post(self):
        """
            Upload a Student's Grade in a Course - Admins Only
        """
        data = student_grades_namespace.payload

        student = Student.get_by_id(id=data['student_id'])
        course = Course.get_by_id(id=data['course_id'])
        
        # Confirm that the student is taking the course
        student_course = StudentCourse.query.filter_by(student_id=student.id, course_id=course.id).first()
        if not student_course:
            return {"message": f"{student.first_name} {student.last_name} is not taking {course.name}"}, HTTPStatus.NOT_FOUND
        
        # Add a new grade
        new_grade = Score(
            student_id = data['student_id'],
            course_id = data['course_id'],
            score = data['score'],
            grade = get_letter_grade(data['score'])
        )

        new_grade.save()

        grade_resp = {}
        grade_resp['grade_id'] = new_grade.id
        grade_resp['student_id'] = new_grade.student_id
        grade_resp['student_first_name'] = student.first_name
        grade_resp['student_last_name'] = student.last_name
        grade_resp['admission_no'] = student.admission_no
        grade_resp['course_id'] = new_grade.course_id
        grade_resp['course_name'] = course.name
        grade_resp['course_teacher'] = course.teacher_id
        grade_resp['score'] = new_grade.score
        grade_resp['grade'] = new_grade.grade

        return grade_resp, HTTPStatus.CREATED
        
        
@student_grades_namespace.route('/grades/<int:student_id>/')
class GetAddUpdateGrades(Resource):

    @student_grades_namespace.doc(
        description = "Retrieve a Student's Grades - Admins or Specific Student Only",
        params = {
            'student_id': "The Student's ID"
        }
    )
    # @jwt_required() 
    def get(self, student_id):
        """
            Retrieve a Student's Grades - Admins or Specific Student Only
        """
        # if is_student_or_admin(student_id):

        # Confirm existence of student
        student = Student.query.filter_by(id=student_id).first()
        if not student:
            return {"message": "Student Not Found"}, HTTPStatus.NOT_FOUND
        
        # Retrieve the student's grades        
        courses = StudentCourse.get_student_courses(student_id)
        resp = []

        for course in courses:
            grade_resp = {}
            grade_in_course = Score.query.filter_by(student_id=student_id, course_id=course.id ).first()
            
            grade_resp['course_name'] = course.name

            if grade_in_course:
                grade_resp['grade_id'] = grade_in_course.id
                grade_resp['score'] = grade_in_course.score
                grade_resp['letter_grade'] = grade_in_course.grade
            else:
                grade_resp['percent_grade'] = None
                grade_resp['letter_grade'] = None
            
            resp.append(grade_resp)
        
        return resp, HTTPStatus.OK
    
    # else:
    #     return {"message": "Admins or Specific Student Only"}, HTTPStatus.FORBIDDEN
    
    
    

@student_grades_namespace.route('/cgpa/<int:student_id>/')
class GetStudentCGPA(Resource):

    @student_grades_namespace.doc(
        description = "Calculate a Student's CGPA - Admins or Specific Student Only",
        params = {
            'student_id': "The Student's ID"
        }
    )
    # @jwt_required()
    def get(self, student_id):
        """
            Calculate a Student's CGPA - Admins or Specific Student Only
        """
        # if is_student_or_admin(student_id):

        student = Student.get_by_id(student_id)
        
        courses = StudentCourse.get_student_courses(student_id)
        total_gpa = 0
        
        for course in courses:
            grade = Score.query.filter_by(
                    student_id=student_id, course_id=course.id
                ).first()
            
            if grade:
                grade = grade.grade
                gpa = convert_grade_to_gpa(grade)
                total_gpa += gpa
            
        cgpa = total_gpa / len(courses)
        round_cgpa = float("{:.2f}".format(cgpa))

        return {"message": f"{student.first_name} {student.last_name}'s CGPA is {round_cgpa}"}, HTTPStatus.OK






