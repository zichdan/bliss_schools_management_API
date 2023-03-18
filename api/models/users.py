from ..utils import db
import uuid
from datetime import datetime
import random

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.Text(), nullable=False)
    user_type = db.Column(db.String(15))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    __mapper_args__ = {
        'polymorphic_on': user_type,
        'polymorphic_identity': 'user'
    }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        

    def update(self):
        db.session.commit()
        
        
    def __repr__(self):
        return f"User <{self.email}>"
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)




class Admin(User):
    __tablename__ = 'admins'
    id = db.Column(db.Integer(), db.ForeignKey('users.id'), primary_key=True)
    admin_key = db.Column(db.String(20), nullable=False, default=str(uuid.uuid4()), unique=True)


    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    

class Student(User):
    __tablename__ = 'students'
    id = db.Column(db.Integer(), db.ForeignKey('users.id'), primary_key=True)
    admission_no = db.Column(db.String(50), unique=True)
    courses = db.relationship('Course', secondary='student_courses')
    score = db.relationship('Score', backref="student_score", lazy=True)

    __mapper_args__ = {
        'polymorphic_identity': 'student'
    }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)


class Teacher(User):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer(), db.ForeignKey('users.id'), primary_key=True)
    staff_no = db.Column(db.Integer(), nullable=False, default=random.randint(1, 100), unique=True,)
    courses = db.relationship('Course', backref='teacher_course')

    __mapper_args__ = {
        'polymorphic_identity': 'teacher'
    }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def update(self):
        db.session.commit() 

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)


#     def __repr__(self):
#         return f"<{self.name}>"

    
#     @classmethod
#     def get_by_id(cls, id):
#         return cls.query.get_or_404(id)



# from ..utils import db

# import uuid




# class Admin(db.Model):
#     __tablename__= "admin"
#     id = db.Column(db.Integer(), primary_key=True)
#     username = db.Column(db.String(),unique=True, nullable=False)
#     email = db.Column(db.String(), unique=True, nullable=False)
#     password_hash = db.Column(db.Text(),nullable=False)
#     admin_key = db.Column(db.String(100), nullable=False, default=str(uuid.uuid4()))

    
    
#     import random

# class Admin(db.Model):
#     __tablename__= "admin"
#     id = db.Column(db.Integer(), primary_key=True)
#     username = db.Column(db.String(),unique=True, nullable=False)
#     email = db.Column(db.String(), unique=True, nullable=False)
#     password_hash = db.Column(db.Text(),nullable=False)
#     admin_key = db.Column(db.Integer(), nullable=False, default=random.randint(1, 4)))
    
    
#     def __repr__(self):
#         return f"<User {self.username}>"
    
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
        


#     @classmethod
#     def get_by_id(cls, id):
#         return cls.query.get_or_404(id)

