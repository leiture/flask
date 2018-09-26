from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    """项目配置类"""
    # 数据库链接配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/test4"
    # 开启数据库跟踪操作
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 设置加密字符串
    SECRET_KEY = "SAKLDLASKJDLASDSAKNJDJK9U898AS8D8"


#1.创建app对象
app = Flask(__name__)
app.config.from_object(Config)

#2.创建数据库对象
db = SQLAlchemy(app)

"""
mytable = Table("mytable", metadata,
                        Column('mytable_id', Integer, primary_key=True),
                        Column('value', String(50))
                   )
"""
# 使用第三张表来维护学生表和选课表之间的多对多的关系
tb_student_course = db.Table('tb_student_course',
        db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
        db.Column('course_id', db.Integer, db.ForeignKey('courses.id')))

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)

    """
       # 定义关系字段
       # student.courses : 该学生选修了那些课程
       # course.students : 该课程被那些学生选修了
       # secondary： 将第三张关系表的表名称赋值

       if stu.courses:
           # 查询对象有值 表示查询数据库成功，

       lazy: 懒加载  dynamic：动态查询 （提高性能）
       如果添加了lazy="dynamic"属性，那么在使用stu.courses就会变成懒加载的形式
       如果没有用到该数据，就不会真正的去数据库查询只会返回orm.dynamic.AppenderBaseQuery对象
       如果真正用到该数据[stu.courses.all()],才会去数据库查询
       stu.courses --》AppenderBaseQuery对象
       stu.courses.all() --》[Course: 3  生物, Course: 1  化学, Course: 2  物理]
       """
    courses = db.relationship('Course',
                              backref= 'students',
                              secondary = tb_student_course,
                              lazy = 'dynamic')

    def __repr__(self):
        return 'Students: %s  %s'%(self.id, self.name)


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)

    def __repr__(self):
        return 'Course: %s  %s'%(self.id, self.name)

if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    # 添加测试数据

    stu1 = Student(name='张三')
    stu2 = Student(name='李四')
    stu3 = Student(name='王五')

    cou1 = Course(name='物理')
    cou2 = Course(name='化学')
    cou3 = Course(name='生物')

    stu1.courses = [cou2, cou3]
    stu2.courses = [cou2]
    stu3.courses = [cou1, cou2, cou3]

    db.session.add_all([stu1, stu2, stu2])
    db.session.add_all([cou1, cou2, cou3])

    db.session.commit()

    app.run(debug=True)