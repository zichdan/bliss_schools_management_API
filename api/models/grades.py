from ..utils import db
from datetime import datetime


class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer(), primary_key=True)
    student_id = db.Column(db.Integer(), db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer(), db.ForeignKey('courses.id'))
    score = db.Column(db.Float, nullable=False)
    grade = db.Column(db.Float(), nullable=True)
    created_at = db.Column(db.DateTime() , nullable=False , default=datetime.utcnow)

    def __repr__(self):
        return f"<{self.score}%>"
        
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
        
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
 
    
# class Grade(db.Model):
#     __tablename__ = 'scores'

#     id = db.Column(db.Integer, primary_key=True)
#     student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
#     course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
#     score = db.Column(db.Float , nullable=False)
#     gpa = db.Column(db.String(5) , nullable=True )
#     created_at = db.Column(db.DateTime() , nullable=False , default=datetime.utcnow)

#     def __init__(self, student_id, course_id, score, gpa):
#         self.student_id = student_id
#         self.course_id = course_id
#         self.score = score
#         self.gpa = gpa
   

#     def save(self):
#         db.session.add(self)
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()

#     @classmethod
#     def get_by_id(cls, id):
#         return cls.query.get_or_404(id)