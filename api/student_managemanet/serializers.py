from flask_restx import fields



student_signup_field =  {
    'first_name': fields.String(required=True, description="Student's First Name"),
    'last_name': fields.String(required=True, description="Students's Last Name"),
    'email': fields.String(required=True, description="Student's Email"),
    'password': fields.String(required=True, description="Student's Temporary Password"),
    # 'admission_no': fields.String(required=True, description="Student's admission Number")
}

student_retrieve_field =  {
    'id': fields.Integer(),
    'first_name': fields.String(required=True, description="First Name"),
    'last_name': fields.String(required=True, description="Last Name"),
    'email': fields.String(required=True, description="Student's Email"),
    'adission_no': fields.String(required=True, description="Student's admission no"),
    'user_type': fields.String(required=True, description="Type of student"),
    'admission_no': fields.String(required=True, description="Student's Matriculation Number")    
    }