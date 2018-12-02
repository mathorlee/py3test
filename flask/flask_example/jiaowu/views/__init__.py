from flask_example import app

from flask_example.jiaowu.models import Student

@app.route("/jiaowu/student/")
def student():
    students = Student.query.all()

    return "Hello World!"