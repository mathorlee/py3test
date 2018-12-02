from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

from flask import Response

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('flask_example.config')
print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)

from .models import Student, Cource, Teacher, Score

@app.route('/')
def index():
    # s = Student(name='lisongsong')
    # session = Student.query.session
    # session.add(s)
    # session.commit()

    students = Student.query.all()
    records = []
    for student in students:
        records.append(student.to_string())
    data = {'records': records}
    return Response(response=json.dumps(data))

# 查看外键约束
'''
select CONSTRAINT_NAME, TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_SCHEMA, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
from INFORMATION_SCHEMA.KEY_COLUMN_USAGE
where CONSTRAINT_SCHEMA = 'test' and CONSTRAINT_NAME != 'PRIMARY';
'''
