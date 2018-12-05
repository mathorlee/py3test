from flask_example import db
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref

# Column = db.Column
# Integer = db.Integer
# String = db.String

score = db.Table(
    'score',
    # db.metadata,
    Column('student_id', ForeignKey('student.id'), nullable=False),
    Column('cource_id', ForeignKey('cource.id'), nullable=False),
    Column('score', Integer, default=0),
    UniqueConstraint('student_id', 'cource_id')
)

class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(80), unique=False, nullable=False)
    # scores = relationship('')

    def to_string(self):
        # return '<User %r>' % self.name
        return {'name': self.name}

    def __repr__(self):

        return '<User %r>' % self.name

class Cource(db.Model):
    __tablename__ = 'cource'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teacher.id'), nullable=False)
    teacher = relationship('Teacher', backref=backref('cources', order_by=id))

    students = relationship('Student', secondary=score, backref=backref('cources'))

    def __repr__(self):
        return '<Cource(name=%s)>' % self.name


class Teacher(db.Model):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)

    def __repr__(self):
        return '<Teacher(name=%s)>' % self.name

class Score2(db.Model):
    __tablename__ = 'score2'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, nullable=False)
    cource_id = Column(Integer, nullable=False)
    score = Column(Integer, default=0, nullable=False)

    def __repr__(self):
        return '<Score()>'