import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.users import User, Admin, Teacher, Student 
# import pytest

class UserTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config=config_dict['test'])
        
        self.appctx =self.app.app_context()
        
        self.appctx.push()
        
        self.client =self.app.test_client()        
        
        db.create_all()


    def tearDown(self):
        db.drop_all()
        
        self.appctx.pop()
        
        self.app = None
        
        self.client = None
        
        

    def test_admin_Registration(self):

    # Register an admin
        admin_signup_data = {
            "first_name": "stafffirstname",
            "last_name": "stafffirstname",
            "email": "testadmin@gmail.com",
            "password": "password",
            "user_type": "admin"
        }
        response = self.client.post('/staff/signup/admin', json=admin_signup_data)
                
        admin = Admin.query.filter_by(email="testadmin@gmail.com").first()
            
        assert admin.first_name == "stafffirstname"
        
        assert admin.last_name == "stafffirstname"

            
        assert response.status_code == 201
            
            
        #                      #  What i learned while trying to debug
        # admin = Admin.query.filter_by(email="testadmin@gmail.com").first()
        # if admin is not None:
        #     assert admin.first_name == "stafffirstname"
        # else:
        #     pytest.fail("Could not find staff member with email 'testuser@company.com'")

          
    # def test_login_staff(self):
    #     data = {
    #         "email":"teststaff.com",
    #         "password": "password"
    #     }
        
    #     response = self.client.post('/auth/login', json=data  )# headers=headers)
        
    #     # user = User.query.filter_by(email="teststaff.com")
        
    #     assert response.status_code == 200
                
    #     token = create_access_token(identity=admin.id)

    #     headers = {
    #         "Authorization": f"Bearer {token}"
    #     }



    def test_teacher_Registration(self):
    # Register a teacher
        teacher_signup_data = {
            "first_name": "firstname",
            "last_name": "lastname",
            "email": "testteacher@gmail.com",
            "password": "password",
            "user_type": "teacher"
        }
        token = create_access_token(identity="test_teacher")
        headers = {
            "Authorization": f"Bearer {token}"
        }
            
        response = self.client.post('/staff/signup/teacher', json=teacher_signup_data, headers=headers)
                
        teacher = Teacher.query.filter_by(email="testteacher@gmail.com").first()
            
        assert teacher.first_name == "firstname"
        
        assert teacher.last_name == "lastname"
            
        assert response.status_code == 201

        
        
    def test_login_staff(self):
        # Create an admin user with known credentials
        admin = Admin(
            first_name='Test',
            last_name='Admin',
            email='testadmin@gmail.com',
            password_hash=generate_password_hash('password'),
        )
        # db.session.add(admin)
        admin.save()

        # Provide valid login credentials
        data = {
            "email": "testadmin@gmail.com",
            "password": "password"
        }

        # Post login data to /auth/login
        response = self.client.post('/auth/login', json=data)

        # Check that the response status code is 200
        assert response.status_code == 200

        # Create an access token using the admin user's id
        token = create_access_token(identity=admin.id)

        # Set the Authorization header to the access token
        headers = {
            "Authorization": f"Bearer {token}"
        }

        # # Make a request to a protected resource using the access token
        # response = self.client.get('/admin/dashboard', headers=headers)

        # # Check that the response status code is 200
        # assert response.status_code == 200

            
        
        
        
        
        
        
        
        ### first effort on trying to test the login routes
    # def test_login_staff(self):
    #     data = {
    #         "email":"teststaff.com",
    #         "password": "password"
    #     }
        
    #     response = self.client.post('/auth/login', json=data  )# headers=headers)
        
    #     user = User.query.filter_by(email="teststaff.com")
        
    #     assert response.status_code == 200
             
    #     token = create_access_token(identity=user.id)

    #     headers = {
    #         "Authorization": f"Bearer {token}"
    #     }
            
        # assert user.email == "teststaff.com"
            
        
       