
from ..utils import db
from flask_restx import Namespace, Resource, fields
from .serializers import student_signup_field,student_retrieve_field
from ..models.users import Student
from ..models.courses import StudentCourse
# from ..utils.decorators import admin_required
from werkzeug.security import generate_password_hash
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity


student_namespace = Namespace('students', description='Namespace for Students')

student_signup_model = student_namespace.model('StudentSignup',student_signup_field)

student_model = student_namespace.model('Student', student_retrieve_field)


@student_namespace.route('/students')
class GetAllStudents(Resource):

    @student_namespace.marshal_with(student_model)
    @student_namespace.doc(
        description="Retrieve all students"
    )
    # @admin_required()
    
    def get(self):
        """
            Retrieve all Students - Admins Only
        """
        students = Student.query.all()

        return students, HTTPStatus.OK


# @student_namespace.route('/register')
# class StudentRegistration(Resource):

#     @student_namespace.expect(student_signup_model)
#     @student_namespace.marshal_with(student_model)
    # @admin_required()
    
    # def post(self):
    #     """
    #         Register a Student - Admins Only
    #     """        
    #     data = student_namespace.payload

    #     new_student = Student(
    #         first_name = data['first_name'],
    #         last_name = data['last_name'],
    #         email = data['email'],
    #         password_hash = generate_password_hash(data['password']),
    #         matric_no = data['matric_no'],
    #         user_type = 'student'
    #     )

    #     new_student.save()

    #     return new_student, HTTPStatus.CREATED


@student_namespace.route('/<int:student_id>')
class GetUpdateDeleteStudents(Resource):
    
    @student_namespace.marshal_with(student_model)
    @student_namespace.doc(
        description="Retrieve a student's details by ID",
        params = {
            'student_id': "The Student's ID"
        }
    )
    # @jwt_required()
    def get(self, student_id):
        """
            Retrieve a Student's Details by ID
        """
        student = Student.get_by_id(student_id)
        
        return student, HTTPStatus.OK
    
    
    
    @student_namespace.expect(student_signup_model)
    # @student_namespace.marshal_with(student_model)
    @student_namespace.doc(
        description="Update a student's details by ID",
        params = {
            'student_id': "The Student's ID"
        }
    )
    # @jwt_required()
    def put(self, student_id):
        """
            Update a Student's Details by ID
        """
        data = student_namespace.payload
        
        # student = Student.get_by_id(student_id)
        student = Student.query.filter_by(id=student_id).first()
        if student:
            student.first_name = data['first_name']
            student.last_name = data['last_name']
            student.email = data['email']
            student.password_hash = generate_password_hash(data['password'])

            try:
                student.update()
                
                student_resp = {}  
                student_resp['id'] = student.id
                student_resp['first_name'] = student.first_name
                student_resp['last_name'] = student.last_name
                student_resp['email'] = student.email
                student_resp['admission'] = student.admission_no
                student_resp['user_type'] = student.user_type

                return {
                    'updated_student': student_resp,
                    'message': ' Student {} {} updated successfully'.format(student.first_name,student.last_name ) 
                    }, HTTPStatus.CREATED
            except:
                db.session.rollback()
                return {'message': 'An error occurred while updating student details'}, HTTPStatus.INTERNAL_SERVER_ERROR
        return {'message': 'Student  not found'}, HTTPStatus.NOT_FOUND


    
    
    
    @student_namespace.doc(
        description='Delete a student by ID',
        params = {
            'student_id': "The Student's ID"
        }
    )
    # @admin_required()
    def delete(self, student_id):
        """
            Delete a student by ID - Admins Only
        """
        student = Student.get_by_id(student_id)

        student.delete()

        return {"message": "Student Successfully Deleted"}, HTTPStatus.OK
    
    
@student_namespace.route('/<int:student_id>/courses')
class GetStudentCourses(Resource):

    @student_namespace.doc(
        description = "Retrieve a Student's Courses - Admins or Specific Student Only",
        params = {
            'student_id': "The Student's ID"
        }
    )
    # @jwt_required()
    def get(self, student_id):
        """
            Retrieve a Student's Courses - Admins or Specific Student Only
        """
        # if is_student_or_admin(student_id):
            
        courses = StudentCourse.get_student_courses(student_id)
        resp = []

        for course in courses:
            course_resp = {}
            course_resp['id'] = course.id
            course_resp['name'] = course.name
            course_resp['teacher'] = course.teacher_id

            resp.append(course_resp)

        return resp, HTTPStatus.OK
    
        # else:
        #     return {"message": "Admins or Specific Student Only"}, HTTPStatus.FORBIDDEN
