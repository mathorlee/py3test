import re


s = '李彦龙,李浩鹏,李天一,李铁刚,李君昊,李国艳,李恩德,李文雅,李文轩,李文博,李文璇,李文萱,李文渲,李美红,李雨洁,李诗蕊,李泊萱,李可昕,李章洪,李亚萍,李智博,李子宸,李鸿娜,李玉锁,李宏娜,李金煜,李艾玲,李绿峰,李子昊,李慧,李娜,李建中,李亚蒙,李亚梦,李中山,李汉煜,李越泽,李维哲,李逸,李乾,李赟,李淩'
student_names = s.split(',')
# print('学生个数: ', len(student_names))

cource_names = ['语文', '数学', '英语', '历史', '地理', '计算机', '化学', '体育']

teacher_names = ['李老师', '王老师', '张老师', '赵老师', '张三', '李四', '王五', '査老师', '哼哈老师', '兵长老师']

import random

def random_sex():
    r = random.randint(0, 1)
    if r == 0:
        return 'M'
    return 'F'

def random_birth():
    year = random.randint(1980, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 30)
    return '%s%02d%02d' % (year, month, day)
