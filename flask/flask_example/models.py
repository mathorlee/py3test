from flask_example import db

Column = db.Column
Integer = db.Integer
String = db.String

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    def to_string(self):
        # return '<User %r>' % self.name
        return {'name': self.name}

    def __repr__(self):

        return '<User %r>' % self.name

class Cource(db.Model):
    __tablename__ = 'cource'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    teacher_id = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Cource(name=%s)>' % self.name


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)

    def __repr__(self):
        return '<Teacher(name=%s)>' % self.name


class Score(db.Model):
    __tablename__ = 'score'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, nullable=False)
    cource_id = Column(Integer, nullable=False)
    score = Column(Integer, default=0, nullable=False)

    def __repr__(self):
        return '<Score()>'