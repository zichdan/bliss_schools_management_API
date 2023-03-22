from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_restx import Api
from flask_migrate import Migrate

from .config.config import config_dict
from .utils import db
from .utils.blocklist import BLOCKLIST

from .course_management.course import course_namespace
from .auth.admin import auth_namespace
from .student_managemanet.students import student_namespace
from .grades_management.grade import student_grades_namespace
from .staff_management.admin import admin_namespace

from .models.users import User, Admin, Student, Teacher
from .models.courses import Course, StudentCourse
from .models.grades import Score

from flask_jwt_extended import JWTManager
from werkzeug.exceptions import NotFound, MethodNotAllowed
from http import HTTPStatus


def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    
    app.config.from_object(config)
    
    db.init_app(app)
    
    load_dotenv()
    
    
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    
    api = Api(app)


    authorizations = {
            "Bearer Auth": {
                "type": "apiKey",
                "in": "header",
                "name": "Authorization",
                "description": "Add a JWT token to the header with ** Bearer &lt;JWT&gt; ** token to authorize"
            }
        }

    # api = Api(
    #     app,
    #     title='Student Management API',
    #     description='A student management REST API service',
    #     authorizations=authorizations,
    #     security='Bearer Auth'
    #     )

     
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST
    
    
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
               { "description": "The token has being revoked.", 
                 "error": "token_revoked"
                }
            ), 
            401,
        )
        

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh",
                    "error": "fresh_token_required."
                }
            ),
            401,
        )
        
    
    # @jwt.additional_claims_loader
    # def add_claims_to_jwt(identity):
    #     # Look in the database and check if the user is an admin
    #     if identity == 5:
    #         return {"is_admin": True}
    #     return {"is_admin": False}
        
    
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )


    api.add_namespace(auth_namespace, path='/auth')
    api.add_namespace(admin_namespace, path='/admin')
    api.add_namespace(course_namespace, path='/courses')
    api.add_namespace(student_namespace, path='/students')
    api.add_namespace(student_grades_namespace, path='/grades')
    
     
    @api.errorhandler(NotFound)
    def not_found(error):
        return {"error": "Not Found"}, 404
    
    
    @api.errorhandler(MethodNotAllowed)
    def method_not_allowed(error):    
        return {"error": "Method_Not_Allowed"}, 405
    
    
    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User': User,
            'Admin': Admin,
            'Student': Student,
            'Teacher': Teacher,
            'Course': Course,
            'StudentCourse': StudentCourse,
            'Score': Score
        }
        
    return app

