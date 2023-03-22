from datetime import datetime
from flask import request
from flask_restx import Namespace, Resource
from ..models.users import User, Admin, Teacher, Student
from ..utils.blocklist import BLOCKLIST
from ..utils import db
from ..utils import user_decorators
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from .serializers import login_fields_serializer, all_users_fields_serializer, signUp_fields_serializer
from http import HTTPStatus


admin_namespace = Namespace('admin', description="Namespace for admin")

signup_model = admin_namespace.model('Signup', signUp_fields_serializer)
login_model = admin_namespace.model('Login', login_fields_serializer)
user_model = admin_namespace.model('Login', all_users_fields_serializer)




@admin_namespace.route('/signup/admin')
class AdminSignUp(Resource):
    @admin_namespace.expect(signup_model)
    def post(self):
        """
            Register an Administrator 
        """
        data = request.get_json()

        
        # check if user already exists
        user = User.query.filter_by(email=data.get('email')).first()
        if user:
            # check if admin already exists
            admin = Admin.query.filter_by(email=data.get('email', None)).first()
            if admin:
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