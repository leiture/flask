# -*-charset utf-8-*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import not_,or_,and_


class Config(object):
    DEBUG = True
    # mysql数据库链接配置
    # 格式: mysql://账号:密码@ip地址:端口号/数据库名称
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/test'
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 动态追踪修改设置，如未设置只会提示警告
    # SQLALCHEMY_ECHO = True


app = Flask(__name__)
# 将配置信息关联到app中
app.config.from_object(Config)
# 2.创建数据库对象
db = SQLAlchemy(app)


# 3.使用自定义模型类的方法创建数据库的表，继承：db.Model
class Role(db.Model):
    # 使用__tablename__自定义表名称, 如果不设置默认值是类名的小写role
    __tablename__ = 'roles'
    # id字段 db.Integer: 32位的整型数据   primary_key=True: 设置该字段为主键
    id = db.Column(db.Integer, primary_key=True)
    # name字段 db.String(128): 128位的字符串类型  unique=True: 设置字段的唯一性
    name = db.Column(db.String(128), unique=True)
    """
       定义关系字段 该字段并不是数据库一列，在数据库并不存在，
       只是在flask代码层面方便我们查询而定义的字段

       role = Role()
       role.users : 该角色下面有那些用户

       user = User()
       user.role ：该用户属于那种角色

       backref: 反向引用，给User对象使用
       """
    users = db.relationship('User', backref='roles')

    def __repr__(self):
        """
        自定义格式化输出
        没有重写该方法：
        role = Role()   print(role)  ---> object对象
        重写该方法:
        role = Role()   print(role)  ---> "Role: xx xx "
        """
        return 'Role:%s  %s' % (self.id, self.name)


class User(db.Model):
    """用户表  多 """
    __tablename__ = 'users'
    # id字段
    id = db.Column(db.Integer, primary_key=True)
    # name字段
    name = db.Column(db.String(128), unique=True)
    # email
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64), unique=True)
    # 创建外键
    # "roles.id" --> 数据库层面的理解 roles表的id作为外键关联起来
    # Role.id --> 面向对象层面理解 Role类的id属性作为外键关联起来
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    def __repr__(self):
        return 'User:%s  %s  %s  %s  %s' % (self.id, self.name, self.email, self.password, self.role_id)


if __name__ == '__main__':
    # 删除数据库所有表
    db.drop_all()
    # 创建所有表
    db.create_all()
    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()

    ro2 = Role(name='user')
    db.session.add(ro2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
    us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
    us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
    us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
    us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
    us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    db.session.commit()

    app.run()

    """
     查询所有用户数据
     User.query.all()

     查询有多少个用户
     User.query.count()

     查询第1个用户
     User.query.get(1)

     查询id为4的用户[3种方式]
     User.query.get(4)

     # 使用filter_by精确查询
     # id:就是属于User类  first: 获取一条数据
     User.query.filter_by(id=4).first()

     # 使用filter查询，
     # 必须指明id来至于那个类：User.id
     User.query.filter(User.id==4).first()

     查询名字结尾字符为g的所有数据[开始startswith/包含contains]

      User.query.filter(User.name.endswith('g')).all()

      User.query.filter(User.name.contains('g')).all()

     查询名字不等于wang的所有数据[2种方式]
     # 使用!=符号 （常用）
     User.query.filter(User.name!="wang").all()
     # 需要导入 from sqlalchemy import not_
     User.query.filter(not_(User.name=="wang")).all()

     查询名字和邮箱都以 li 开头的所有数据[2种方式]

     User.query.filter(User.name.startswith('li'), User.email.startswith('li')).all()

     User.query.filter(and_(User.name.startswith('li'), User.email.startswith('li'))).all()


     查询password是 `123456` 或者 `email` 以 `itheima.com` 结尾的所有数据

     # 必须要导入 from sqlalchemy import or_
     User.query.filter(or_(User.password=="123456", User.email.endswith('itheima.com'))).all()


     查询id为 [1, 3, 5, 7, 9] 的用户列表
     # in_([]) 包含操作
     User.query.filter(User.id.in_([1,3,5,7,9])).all()

     查询name为liu的角色数据
     User.query.filter(User.name == "liu").first()

     查询所有用户数据，并以邮箱降序排序
     # 借助order_by函数进行排序  desc：降序 aesc: 升序
     User.query.order_by(User.email.desc()).all()

     将所有数据分页，每页3个，查询第2页的数据(重点)
     paginate = User.query.paginate(2, 3)

     # 获取当前页页码的所有数据
     paginate.items

     # 获取当前页码
     paginate.page

     # 获取总页数
     paginate.pages

     """
