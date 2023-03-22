from flask_restx import fields


signUp_fields_serializer = {
    'email': fields.String(required=True, description='User email address'),
    'first_name': fields.String(required=True, description="First name"),
    'last_name': fields.String(required=True, description="Last name"),
    'password': fields.String(required=True, description="A password"),
    'user_type': fields.String(required=True, description="Type of user"),
}


admin_fields_serializer = {
        'id': fields.Integer(),
        'first_name': fields.String(required=True, description="Username"),
        'last_name': fields.String(required=True, description="Username"),
        'email': fields.String(required=True, description="User's email"),
        'user_type': fields.String(required=True, description="type of user['admin','student', 'teacher']"), 
        'created_at': fields.String(required=True, description="type of user['admin','student', 'teacher']"), 
        'admin_key': fields.String(required=True, description="type of user['admin','student', 'teacher']")
}

teacher_fields_serializer = {
        'id': fields.Integer(),
        'first_name': fields.String(required=True, description="Username"),
        'last_name': fields.String(required=True, description="Username"),
        'email': fields.String(required=True, description="User's email"),
        'user_type': fields.String(required=True, description="type of user['admin','student', 'teacher']"), 
        'created_at': fields.String(required=True, description="type of user['admin','student', 'teacher']"), 
        'staff_no': fields.String(required=True, description="Type of user")
}       
        
        