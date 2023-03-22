from flask_restx import fields


student_signup_field = {
    'email': fields.String(required=True, description='User email address'),
    'first_name': fields.String(required=True, description="First name"),
    'last_name': fields.String(required=True, description="Last name"),
    'password': fields.String(required=True, description="A password"),
    'user_type': fields.String(required=True, description="Type of user"),
}



student_update_field =  {
    'first_name': fields.String(required=True, description="Student's First Name"),
    'last_name': fields.String(required=True, description="Students's Last Name"),
    'email': fields.String(required=True, description="Student's Email"),
    'password': fields.String(required=True, description="Student's Temporary Password"),
}

student_retrieve_field =  {
    'id': fields.Integer(),
    'first_name': fields.String(required=True, description="First Name"),
    'last_name': fields.String(required=True, description="Last Name"),
    'email': fields.String(required=True, description="Student's Email"),
    'user_type': fields.String(required=True, description="Type of student"),
    'admission_no': fields.String(required=True, description="Student's Admission Number")    
    }



student_course_model_field = {
        'student_id': fields.Integer(description="Student's User ID"),
        'course_id': fields.Integer(description="Course's ID")
    }



grade_model_field = {
        'id': fields.Integer(description="Grade ID"),
        'course_id': fields.Integer(required=True, description="Course ID"),
        'percent_grade': fields.Float(required=True, description="Grade in Percentage: Number Only")       
    }


# grade_update_model =  {
#         'percent_grade': fields.Float(required=True, description="Grade in Percentage: Number Only")       
#     }
