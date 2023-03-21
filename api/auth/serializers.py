from flask_restx import fields



login_fields_serializer = {
    'email': fields.String(required=True, description='User email address'),
    'password': fields.String(required=True, description='User password')
}


signUp_fields_serializer = {
    'email': fields.String(required=True, description='User email address'),
    'first_name': fields.String(required=True, description="First name"),
    'last_name': fields.String(required=True, description="Last name"),
    'password': fields.String(required=True, description="A password"),
    'user_type': fields.String(required=True, description="Type of user"),
}


all_users_fields_serializer = {
        'id': fields.Integer(),
        'first_name': fields.String(required=True, description="Username"),
        'last_name': fields.String(required=True, description="Username"),
        'email': fields.String(required=True, description="User's email"),
        'password_hash': fields.String(required=True, description="Password") ,
        'user_type': fields.String(required=True, description="type of user['admin','student', 'teacher']"), 
        'created_at': fields.String(required=True, description="type of user['admin','student', 'teacher']"), 
        'staff_no': fields.String(required=True, description="Type of user"),
        'admin_key': fields.String(required=True, description="type of user['admin','student', 'teacher']"),         'admin_key': fields.String(required=True, description="type of user['admin','student', 'teacher']"), 
        'admisson_no': fields.String(required=True, description="type of user['admin','student', 'teacher']"),         'admin_key': fields.String(required=True, description="type of user['admin','student', 'teacher']") 
    }