from flask_restx import fields



course_model_field = {
        'id': fields.Integer(description="Course's ID"),
        'name': fields.String(description="Course's Name", required=True),
        'teacher_id': fields.Integer(description="Teacher ID taking the Course", required=True)
    }

# student_model_field = {
#         'course_id': fields.Integer(description="Course's ID"),
#         'student_id': fields.Integer(description="Student's User ID")
#     }



course_retrieve_fields_serializer =  {
    'id': fields.Integer(),
    'name': fields.String(required=True, description="A course name"),
    'course_code': fields.String(description="A course code"),
    'teacher_id': fields.Integer (),
    'created_at': fields.DateTime( description="Course creation date"),
}


student_course_field = {
    'student_id': fields.Integer(description="Student's User ID"),
    'course_id': fields.Integer(description="Course's ID")
}

