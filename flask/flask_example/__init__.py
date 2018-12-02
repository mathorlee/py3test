from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('flask_example.config')
print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)

from .models import Student

@app.route('/')
def index():
    students = Student.query.all()
    records = []
    for student in students:
        records.append(student.__repr__())
    return json.dumps(records)