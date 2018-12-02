from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('flask_example.config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# print(app.config)
print(app.config['SQLALCHEMY_DATABASE_URI'])

from flask_example.jiaowu.models import Student

@app.route("/")
def hello():
    students = Student.query.all()
    return "Hello World!"

if __name__ == '__main__':
    app.run()
