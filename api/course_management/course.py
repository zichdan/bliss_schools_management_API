from ..utils import db
from flask import request
from flask_restx import Namespace, Resource
from ..models.courses import Course, StudentCourse
from ..models.users import User, Student, Teacher, Student
from ..utils.user_decorators import admin_required
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt, verify_jwt_in_request
from functools import wraps
from .serializers import course_model_field, course_retrieve_fields_serializer, student_course_field

course_namespace = Namespace('courses', description='Namespace for Courses')


course_model = course_namespace.model('Course', course_model_field)
# student_course_model = course_namespace.model('Student', student_model_field)
course_retrieve_model = course_namespace.model('Display_courses', course_retrieve_fields_serializer)
student_course_model = course_namespace.model('StudentCourse', student_course_field)

@course_namespace.route('')
class GetCreateCourse(Resource):

    @course_namespace.marshal_with(course_retrieve_model)
    @course_namespace.doc(
         description=""" 'Get All Courses'
            This endpoint is accessible to all users. 
            It allows the retrieval of all available courses
            """
    )
    # @jwt_required()
    def get(self):
        """
            Get All Courses
        """
        courses = Course.query.all()

        return courses, HTTPStatus.OK
    
    
    @course_namespace.expect(course_model)
    @course_namespace.doc(
        description="""  'Register a course'
            This endpoint is accessible to an admin . 
            It allows admin create a new course
            """
    )
    # @admin_required()
    def post(self):
        """
            Register a Course
        """
        data = request.get_json()
        teacher = Teacher.query.filter_by(id=data.get('teacher_id')).first()
        if teacher:
            new_course = Course(
                teacher_id = teacher.id,
                name = data.get('name')
            )
          
            course_name = Course.query.filter_by(name=data.get('name')).first()
            if course_name:
                return {
                'message': " A course with same name already exists!"
            }, HTTPStatus.CONFLICT
                              
            course = Course.query.filter_by(teacher_id=data.get('teacher_id')).first()
            if course:
                 return {
                'message': "A teacher acccount with same ID has is linked with A course "
            }, HTTPStatus.CONFLICT

            try:
                new_course.save()
                return {
                    'message': 'Course successfully registered with name as {}'.format(new_course.name) 
                    }, HTTPStatus.CREATED
            except:
                return {'message': 'An error occurred while saving course'}, HTTPStatus.INTERNAL_SERVER_ERROR
        return {'message': 'Invalid teacher id'}, HTTPStatus.UNAUTHORIZED


@course_namespace.route('/<int:course_id>')
class GetUpdateDelete(Resource):
    
    @course_namespace.marshal_with(course_retrieve_model)
    @course_namespace.doc(
        description="Retrieve a course's details by ID",
        params = {
            'course_id': "The Course's ID"
        }
    )
    # @admin_required()
    def get(self, course_id):
        """
            Retrieve a Course's Details by ID
        """
        course = Course.get_by_id(course_id)
        
        return course, HTTPStatus.OK
    
    @course_namespace.expect(course_model)
    @course_namespace.marshal_with(course_retrieve_model)
    @course_namespace.doc(
        description="Update a course's details by ID",
        params = {
            'course_id': "The Course's ID"
        }
    )
#     @admin_required()
    def put(self, course_id):
        """
            Update a Course's Details by ID
        """
        course = Course.get_by_id(course_id)

        data = course_namespace.payload

        course.name = data['name']
        course.teacher_id = data['teacher_id']

        try:
            course.update()
        except:
            db.session.rollback()
            return {'message': 'An error occurred while updating a course'}, HTTPStatus.INTERNAL_SERVER_ERROR
        
        return course, HTTPStatus.OK
    
    
    @course_namespace.doc(
        description='Delete a course by ID',
        params = { 'course_id': "The Course's ID"}
    )
    # @admin_required()
    def delete(self, course_id):
        """
            Delete a course by ID
        """
        course = Course.get_by_id(course_id)

        try:
            course.delete()
        except:
            db.session.rollback()
            return {'message': 'An error occurred while trying to delete the course'}, HTTPStatus.INTERNAL_SERVER_ERROR
        
        return {"message": "Course Successfully Deleted"}, HTTPStatus.OK


@course_namespace.route('/<int:course_id>/students')
class GetStudentEnrollment(Resource):

    # @course_namespace.marshal_with(student_course_model)
    @course_namespace.doc(
        description="Get all students enrolled for a course",
        params = {
            'course_id': "The Course's ID"
        }
    )
    # @admin_required()
    def get(self, course_id):
        """
            Get all Students enrolled for a Course
        """
        # course = Course.get_by_id(course_id) OR
        course = Course.query.filter_by(id=course_id).first()
        if course:
            students_in_course = StudentCourse.get_students_in_course_by(course_id)
        
            resp = []

            for student in students_in_course:
                student_resp = {}
                student_resp['id'] = student.id
                student_resp['first_name'] = student.first_name
                student_resp['last_name'] = student.last_name
                student_resp['admission_no'] = student.admission_no

                resp.append(student_resp)
            return resp, HTTPStatus.OK
        return {'message': 'Course  not found'}, HTTPStatus.NOT_FOUND
        
        
    
    
@course_namespace.route('/studentsEnroll')

class StudentEnrollment(Resource):
    
    
    @course_namespace.expect(student_course_model)
    @course_namespace.doc(
        description="Enroll students for a course")
    
        #   @admin_required()
    def post(self):
        """
            Enroll Students for a Course
        """
        data = course_namespace.payload
        
        
        course = Course.query.filter_by(id=data['course_id']).first()
        if course:
            student = Student.query.filter_by(id=data['student_id']).first()
            if student:
                #check if student has registered for the course before
                check_student_in_course = StudentCourse.query.filter_by(student_id=student.id, course_id=course.id).first()
                if check_student_in_course:
                    return {
                        'message':'{}  {} is already registered for the {}'.format(student.first_name,student.last_name, course.name )
                        } , HTTPStatus.OK
                # Register the student to the course
                enroll_student =  StudentCourse(
                    course_id = course.id,
                    student_id = student.id
                )
                course_student_resp = {}
                course_student_resp['course_id'] = enroll_student.course_id
                course_student_resp['course_name'] = course.name
                course_student_resp['course_teacher'] = course.teacher_id
                course_student_resp['student_id'] = enroll_student.student_id
                course_student_resp['student_first_name'] = student.first_name
                course_student_resp['student_last_name'] = student.last_name
                course_student_resp['student-admission_no'] = student.admission_no
                
                try:
                    enroll_student.save()
                    return {
                        'student_data':course_student_resp,
                        'message': ' Student {} {} registered in Course successfully'.format(student.first_name,student.last_name ) 
                        }, HTTPStatus.CREATED
                except:
                    db.session.rollback()
                    return {'message': 'An error occurred while registering course'}, HTTPStatus.INTERNAL_SERVER_ERROR
            return {'message': 'Student  not found'}, HTTPStatus.NOT_FOUND
        return {'message': 'Course  not found'}, HTTPStatus.NOT_FOUND
    
    
    
    @course_namespace.expect(student_course_model)
    @course_namespace.doc(
        description='Remove a Student from a Course',
    )
    # @admin_required()
    def delete(self):
        """
            Remove a Student from a Course - Admins Only
        """
        data = course_namespace.payload

        # Confirm existence of student and course
        course = Course.query.filter_by(id=data['course_id']).first()
        if course:
            student = Student.query.filter_by(id=data['student_id']).first()
            if student:
                #check if student has registered for the course before
                check_student_in_course = StudentCourse.query.filter_by(student_id=student.id, course_id=course.id).first()
                if check_student_in_course:
                    try:
                        check_student_in_course.delete()
                        return {'message': ' Student {} {} deleted from Course successfully'.format(student.first_name,student.last_name ) 
                            }, HTTPStatus.OK
                    except:
                        db.session.rollback()
                        return {'message': 'An error occurred while deleting the course'}, HTTPStatus.INTERNAL_SERVER_ERROR
                return {
                'message':'{}  {} is not registered in {}'.format(student.first_name,student.last_name, course.name )
                } , HTTPStatus.OK
                
            return {'message': 'Student  not found'}, HTTPStatus.NOT_FOUND
        return {'message': 'Course  not found'}, HTTPStatus.NOT_FOUND
        
                    
        
        
        # course = Course.query.filter_by(id=course_id).first()
        # student = Student.query.filter_by(id=student_id).first()
        # if not student or not course:
        #     return {"message": "Student or Course Not Found"}, HTTPStatus.NOT_FOUND
        
        # # Check if student is not registered for the course
        # student_in_course = StudentCourse.query.filter_by(
        #         student_id=student.id, course_id=course.id
        #     ).first()
        # if not student_in_course:
        #     return {
        #         "message": f"{student.first_name} {student.last_name} is not registered for {course.name}"
        #     }, HTTPStatus.NOT_FOUND

        # # Remove the student from the course
        # student_in_course.delete()

        # return {"message": f"{student.first_name} {student.last_name} has been successfully removed from {course.name}"}, HTTPStatus.OK



# @course_namespace.route('/studentErollment')
# # @course_namespace.marshal_with(course_retrieve_model)

# class EnrollmentID(Resource):

#     def get(self):
#             """
#                 Retrieve a Course's Details by ID
#             """
#             course = StudentCourse.query.all()
#             # course = StudentCourse.get_by_id(StudentCourse_id)
            
#             return course, HTTPStatus.OK