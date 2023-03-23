from datetime import datetime
from flask import request
from flask_restx import Namespace, Resource, fields
from ..models.users import User, Admin, Teacher, Student
from ..utils.blocklist import BLOCKLIST
from ..utils import db
# from ..utils.user_decorators import admin_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from .serializers import login_fields_serializer, all_users_fields_serializer
from http import HTTPStatus


auth_namespace = Namespace('auth', description="Namespace for Authentication")

login_model = auth_namespace.model('Login', login_fields_serializer)
user_model = auth_namespace.model('Marshal_users', all_users_fields_serializer)


            
            
@auth_namespace.route('/login')
class Login(Resource):
    @auth_namespace.expect(login_model)
    def post(self):
        """
            Generate JWT Token
        """
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if not user:
            return {
                'message': 'Invalid email '
            }, HTTPStatus.UNAUTHORIZED
        elif  not check_password_hash(user.password_hash, password):
             return {
                'message': 'Incorrect password'
            }, HTTPStatus.UNAUTHORIZED
        
        access_token = create_access_token(identity=user.email)
        refresh_token = create_refresh_token(identity=user.email)

        response = {
            'message': 'Login Successful',
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        return response, HTTPStatus.OK



@auth_namespace.route('/refresh')
class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        """
            Generate Refresh Token
        """
        user = get_jwt_identity()

        access_token = create_access_token(identity=user)

        return { "access_token": access_token}, HTTPStatus.OK


@auth_namespace.route('/logout')
class Logout(Resource):
    @jwt_required(verify_type=False)
    def post(self):
        """
            Log the User Out by revoking Access/refresh token
        """
        token = get_jwt()
        jti = token['jti']
        token_type = token['type']
        # user_identity = get_jwt_identity()
        try:
            BLOCKLIST.add(jti)
        except:
            return {
                'message': 'An error occurred while saving user'
                }, HTTPStatus.INTERNAL_SERVER_ERROR
        return {"message": f"{token_type.capitalize()} token successfully revoked"}, HTTPStatus.OK
 


@auth_namespace.route('/users')
class GetAll(Resource):

    @auth_namespace.marshal_with(user_model)
    @auth_namespace.doc(
        description="Retrieve all users - Admins Only"
    )
    @jwt_required()
    def get(self):
        """
            Retrieve all Users
        """
        # authenticated_user_id = get_jwt_identity() 
        # admin = Admin.query.filter_by(id=authenticated_user_id).first()   
        # if not admin :
        #     return {'message':'Administrator Access Only'}, HTTPStatus.UNAUTHORIZED
        
        users = User.query.all()

        return users, HTTPStatus.OK
















# @auth_namespace.route('/password-reset-request')
# class PasswordResetRequest(Resource):
#     @auth_namespace.expect(password_reset_request_model)
#     def post(self):
#         """
#             Request for password reset
#         """
#         data = request.get_json()

#         email = data.get('email')

#         user = User.query.filter_by(email=email).first()

#         if not user:
#             return {
#                 'message': 'User does not exist'
#             }, HTTPStatus.NOT_FOUND
#         if user:
#             token = generate_reset_token(25)
#             user.password_reset_token = token
#             db.session.commit()

#             # Send a password reset email
#             send_email(user, token)

#             return {
#                 'message': 'Password reset token generated successfully. Please check your mail!'
#             }, HTTPStatus.OK
    

# @auth_namespace.route('/password-reset/<token>')
# class PasswordReset(Resource):
#     @auth_namespace.expect(password_reset_model)
#     def post(self, token):
#         """
#             Reset password
#         """
#         data = request.get_json()

#         password = data.get('password')
#         confirm_password = data.get('confirm_password')

#         user = User.query.filter_by(password_reset_token=token).first()

#         if not user:
#             return {
#                 'message': 'Invalid or expired token'
#             }, HTTPStatus.BAD_REQUEST

#         if password == confirm_password:
#             hashed_password = generate_password_hash(confirm_password)
#             user.password_hash = hashed_password
#             user.password_reset_token = None
#             db.session.commit()

#             return {
#                 'message': 'Password reset successful'
#             }, HTTPStatus.OK
#         else:
#             return {
#                 'message': 'Passwords do not match'
#             }, HTTPStatus.BAD_REQUEST
