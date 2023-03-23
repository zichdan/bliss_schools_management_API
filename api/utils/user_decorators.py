# from ..models.users import User
# from flask_jwt_extended import  get_jwt_identity, get_jwt, verify_jwt_in_request
# from functools import wraps
# from http import HTTPStatus

# # Get the authorized user type
# def get_user_type(id:int):
#     user = User.query.filter_by(id=id).first()
#     if user:
#         return user.user_type
#     else:
#         return None

# # Custom decorator to verify admin access
# def admin_required():
#     def wrapper(fn):
#         @wraps(fn)
#         def decorator(*args, **kwargs):
#             verify_jwt_in_request()
#             claims = get_jwt()
#             if get_user_type(claims['sub']) == 'admin':
#                 return fn(*args, **kwargs)
#             else:
#                 return {"message": "Administrator access required"}, HTTPStatus.FORBIDDEN
#         return decorator
#     return wrapper



# # Verify student or admin access
# def admin_required(student_id:int) -> bool:
#     claims = get_jwt()
#     active_user_id = get_jwt_identity()
#     if (get_user_type(claims['sub']) == 'admin') or (active_user_id == student_id):
#         return True
#     else:
#         return False

# # Verify student or admin access
# def is_student_or_admin(student_id:int) -> bool:
#     claims = get_jwt()
#     active_user_id = get_jwt_identity()
#     if (get_user_type(claims['sub']) == 'admin') or (active_user_id == student_id):
#         return True
#     else:
#         return False







# from flask_jwt_extended import get_jwt , verify_jwt_in_request
# from functools import wraps
# from flask import jsonify
# from http import HTTPStatus
# from ..models.users import User


# # this function was included here to avoid circular import
# def get_user_type(id:int):
#     """ Get the type a user belong 
#     param:
#         pk : user id
#     """
#     user = User.query.filter_by(id=id).first()
#     if user:
#         return user.user_type
#     else:
#         return None




# def admin_required():
#     """
#     A decorator to protect an endpoint with JSON Web Tokens.

#     Any route decorated with this will require a user type of admin  to be present in the
#     request before the endpoint can be called.
#     """
#     def wrapper(fn):
#         @wraps(fn)
#         def decorator(*args,**kwargs):
#             verify_jwt_in_request()
#             claims = get_jwt()
#             if get_user_type(claims['sub']) == 'admin':
#                 return fn(*args,**kwargs)
#             return jsonify({'message':"Administrator access required!"}) , HTTPStatus.UNAUTHORIZED
#         return decorator
#     return wrapper





# def staff_required():
#     """
#     A decorator to protect an endpoint with JSON Web Tokens.

#     Any route decorated with this will require a user type of admin or teacher  to be present in the
#     request before the endpoint can be called.
#     """
#     def wrapper(fn):
#         @wraps(fn)
#         def decorator(*args,**kwargs):
#             verify_jwt_in_request()
#             claims = get_jwt()
#             if get_user_type(claims['sub']) == 'admin' or get_user_type(claims['sub']) == 'teacher':
#                 return fn(*args,**kwargs)
#             return jsonify({'message': "Admin and Teacher Access Only!" }) , HTTPStatus.UNAUTHORIZED
#         return decorator
#     return wrapper

# def teacherORstudent_required():
#     """
#     A decorator to protect an endpoint with JSON Web Tokens.

#     Any route decorated with this will require a user type of Teacher or Student  to be present in the
#     request before the endpoint can be called.
#     """
#     def wrapper(fn):
#         @wraps(fn)
#         def decorator(*args,**kwargs):
#             verify_jwt_in_request()
#             claims = get_jwt()
#             if get_user_type(claims['sub']) == 'teacher' or get_user_type(claims['sub']) == 'student':
#                 return fn(*args,**kwargs)
#             return jsonify({'message': "Teacher Or Student Access Only!" }) , HTTPStatus.UNAUTHORIZED
#         return decorator
#     return wrapper



# def teacher_required():
#     """
#     A decorator to protect an endpoint with JSON Web Tokens.

#     Any route decorated with this will require a user type of teacher to be present in the
#     request before the endpoint can be called.
#     """
#     def wrapper(fn):
#         @wraps(fn)
#         def decorator(*args,**kwargs):
#             verify_jwt_in_request()
#             claims = get_jwt()
#             if get_user_type(claims['sub']) == 'teacher' :
#                 return fn(*args,**kwargs)
#             return jsonify({'message': "Teacher access Only!" }) , HTTPStatus.UNAUTHORIZED
#         return decorator
#     return wrapper


# def student_required():
#     """
#     A decorator to protect an endpoint with JSON Web Tokens.

#     Any route decorated with this will require a user type of student  to be present in the
#     request before the endpoint can be called.
#     """
#     def wrapper(fn):
#         @wraps(fn)
#         def decorator(*args,**kwargs):
#             verify_jwt_in_request()
#             claims = get_jwt()
#             if get_user_type(claims['sub']) == 'student' :
#                 return fn(*args,**kwargs)
#             return jsonify({'msg': "Student Only!" }) , HTTPStatus.UNAUTHORIZED
#         return decorator
#     return wrapper


# # Custom decorator to verify admin access
# def admin_required():
#     def wrapper(fn):
#         @wraps(fn)
#         def decorator(*args, **kwargs):
#             verify_jwt_in_request()
#             claims = get_jwt()
#             if claims["is_admin"]:
#                 return fn(*args, **kwargs)
#             else:
#                 return {"message": "Administrator access required"}, HTTPStatus.FORBIDDEN
#         return decorator
#     return wrapper