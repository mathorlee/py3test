from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
from create_data import student_names, teacher_names, cource_names, random_birth, random_sex

# engine = create_engine("sqlite:////C:/Users/Administrator/Desktop/db/教务系统", encoding='utf8', echo=True)
engine = create_engine("sqlite:////program/py3test//1.db", encoding='utf8', echo=False)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    birth = Column(String, nullable=False)
    sex = Column(String, nullable=False)

    def __repr__(self):
        return "<Student(name=%s>" % self.name


class Cource(Base):
    __tablename__ = 'cource'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Cource(name=%s)>' % self.name


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return '<Teacher(name=%s)>' % self.name


class Score(Base):
    __tablename__ = 'score'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, nullable=False)
    cource_id = Column(Integer, nullable=False)
    score = Column(Integer, default=0, nullable=False)

    def __repr__(self):
        return '<Score()>'


Base.metadata.create_all(engine)

# p = Student(name='李松松', sex='M', birth='19900306')
# session.add(p)
# session.commit()

# 初始化：每个学生随机选1-n门课程，每个课程随机一个授课老师
# 清空分数，随机分数

student_cource_dict = {}

def clear_db():
    for table in [Student, Teacher, Cource, Score]:
        for row in session.query(table).all():
            session.delete(row)
        session.commit()
    d_student_cource = {}

def init():
    for name in student_names:
        p = Student(name=name, sex=random_sex(), birth=random_birth())
        session.add(p)
    session.commit()

    for name in teacher_names:
        p = Teacher(name=name)
        session.add(p)
    session.commit()

    cnt = 1
    for name in cource_names:
        p = Cource(name=name, teacher_id=cnt)
        cnt += 1
        session.add(p)
    session.commit()

    student_name_id_dict = {}
    cource_name_id_dict = {}
    # p = session.query(Student).filter_by(name='李松松').first()
    for student in session.query(Student).all():
        student_name_id_dict[student.name] = student.id
    for cource in session.query(Cource).all():
        cource_name_id_dict[cource.name] = cource.id

    # 每个学生随机选1-n门课程
    for name in student_names:
        student_cource_dict[name] = []
        cource_cnt = random.randint(2, len(cource_names))
        i = 0
        j = 0
        while i < cource_cnt:
            if random.randint(0, 1):
                i += 1
                student_cource_dict[name].append(cource_names[j])
            j = (j + 1) % len(cource_names)
        print(name, student_cource_dict[name])

    for s_name in student_names:
        for c_name in student_cource_dict[s_name]:
            score = Score(student_id=student_name_id_dict[s_name], cource_id=cource_name_id_dict[c_name], score=random.randint(40, 100))
            session.add(score)
    session.commit()

clear_db()
init()

'''
student()
cource()
score(score, student_id, cource_id)
1. 查询" 01 "课程比" 02 "课程成绩高的学生的信息及课程分数
select student join score where score.cource_id in [1, 2]
'''