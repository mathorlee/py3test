from flask_example import db
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, Date
from sqlalchemy.orm import relationship, backref

# Column = db.Column
# Integer = db.Integer
# String = db.String

# score = db.Table(
#     'score',
#     # db.metadata,
#     Column('student_id', ForeignKey('student.id'), nullable=False),
#     Column('cource_id', ForeignKey('cource.id'), nullable=False),
#     Column('score', Integer, default=0),
#     UniqueConstraint('student_id', 'cource_id'),
# )

class Score(db.Model):
    extend_existing = True

    __tablename__ = 'score'
    student_id = db.Column(Integer, ForeignKey('student.id'), nullable=False, primary_key=True)
    cource_id = db.Column(Integer, ForeignKey('cource.id'), nullable=False, primary_key=True)
    score = db.Column(Integer, default=0)
    # __table_args__ = (
    #     UniqueConstraint('student_id', 'cource_id', name='unique_stuedent_cource'),  # 联合唯一
    # )

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

    students = relationship('Student', secondary=Score, backref=backref('cources'))

    def __repr__(self):
        return '<Cource(name=%s)>' % self.name


class Teacher(db.Model):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)

    def __repr__(self):
        return '<Teacher(name=%s)>' % self.name


class HiveTableStatisticHistoryExt(db.Model):
    '''
    表每天的统计数据
    '''
    __tablename__ = 'hive_tbl_statistic_history_ext'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    metric_key = Column(String(80), nullable=False)  # 指标名字
    metric_value = Column(String(4000), nullable=True) # 指标名字

    __table_args__ = (
        UniqueConstraint('id', 'metric_key', 'date', name='unique_id_key_date'),  # 联合唯一
        Index('index_id_date', 'id', 'date'),  # 联合索引
    )