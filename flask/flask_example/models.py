from flask_example import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    def to_string(self):
        # return '<User %r>' % self.name
        return {'name': self.name}

    def __repr__(self):

        return '<User %r>' % self.name
