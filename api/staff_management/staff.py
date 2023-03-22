from datetime import datetime
from flask import request
from flask_restx import Namespace, Resource
from ..models.users import User, Admin, Teacher, Student
from ..utils.blocklist import BLOCKLIST
from ..utils import db
from ..utils import user_decorators
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from .serializers import  all_users_fields_serializer, signUp_fields_serializer, all_teacher_fields_serializer
from http import HTTPStatus


staff_namespace = Namespace('staff', description="Namespace for staff")

signup_model = staff_namespace.model('Signup', signUp_fields_serializer)
user_model = staff_namespace.model('marshal_users', all_users_fields_serializer)
teachers_model = staff_namespace.model('teachers', all_teacher_fields_serializer)




@staff_namespace.route('/signup/admin')
class AdminSignUp(Resource):
    @staff_namespace.expect(signup_model)
    def post(self):
        """
            Register an Administrator 
        """
        data = request.get_json()

        
        # check if user already exists
        user = User.query.filter_by(email=data.get('email')).first()
        if not user:
            # check if admin already exists
            admin = Admin.query.filter_by(email=data.get('email', None)).first()
            if not admin:
                #create a new administrator
                if data.get( 'user_type')== 'admin':
                    new_admin = Admin(
                        first_name = data.get('first_name'),
                        last_name = data.get('last_name'),
                        email = data.get('email'),
                        password_hash = generate_password_hash(data.get('password')),
                        user_type = 'admin'
                    )
                else:
                    return {
                        'message': 'Input user_type as "admin" '
                    }, HTTPStatus.INTERNAL_SERVER_ERROR    
                  #save new_user
                try:
                    new_admin.save()
                except:
                    db.session.rollback()
                    return {'message': 'An error occurred while saving user'}, HTTPStatus.INTERNAL_SERVER_ERROR
                return {
                        'message': 'User {} created successfully as an {}'.format(new_admin.email, new_admin.user_type)
                    }, HTTPStatus.CREATED
            return {'message': "An administrator acccount with same email already exists"}, HTTPStatus.CONFLICT
        return {'message': "A user with same email already exists"}, HTTPStatus.CONFLICT
    
    
    

@staff_namespace.route('/signup/teacher')
class TeacherSignUp(Resource):
    @staff_namespace.expect(teachers_model)
    def post(self):
        """
            Register a teacher 
        """
        data = request.get_json()

        # check if teacher already exists
        user = User.query.filter_by(email=data.get('email', None)).first()
        if not user:
            # check if teacher already exists
            teacher = Teacher.query.filter_by(email=data.get('email', None)).first()
            if not teacher:
                #create a new teacher
                if data.get('user_type') == 'teacher':
                    new_teacher = Teacher(
                        first_name = data.get('first_name'),
                        last_name = data.get('last_name'),
                        email = data.get('email'),
                        password_hash = generate_password_hash(data.get('password')),
                        user_type = 'teacher'
                    )
                else:
                    return {
                        'message': 'Input user_type as "teacher" '
                    }, HTTPStatus.INTERNAL_SERVER_ERROR    
                    # save new teacher
                try:
                    new_teacher.save()
                except:
                    db.session.rollback()
                    return {'message': 'An error occurred while saving user'}, HTTPStatus.INTERNAL_SERVER_ERROR
                return {'message': 'User {} created successfully as a {}'.format(new_teacher.email, new_teacher.user_type)
                    }, HTTPStatus.CREATED
            return {'message': "A teacher acccount with same email already exists"
                }, HTTPStatus.CONFLICT
        return {'message': "A teacher acccount with same email already exists"
        }, HTTPStatus.CONFLICT
    
    

@staff_namespace.route('/admins')
class GetAllAdmin(Resource):

    @staff_namespace.marshal_with(user_model)
    @staff_namespace.doc(
        description="Retrieve all administrators  - Admins Only"
    )
    def get(self):
        """
            Retrieve all admins
        """
        admin = Admin.query.all()

        return admin, HTTPStatus.OK

    

@staff_namespace.route('/teachers')
class GetAllTeacher(Resource):

    @staff_namespace.marshal_with(user_model)
    @staff_namespace.doc(
        description="Retrieve all teachers  - Admins Only"
    )
    def get(self):
        """
            Retrieve all teachers
        """
        teachers = Teacher.query.all()

        return teachers, HTTPStatus.OK

    
    
    