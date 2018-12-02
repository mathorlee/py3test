from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

@app.route("/")
def index():
    students = Student.query.all()
    return "Hello World!"

if __name__ == '__main__':
    manager.run()
