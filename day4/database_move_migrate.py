#coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

class Config(object):
    """项目配置类"""
    # 数据库链接配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/test3"
    # 开启数据库跟踪操作
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 设置加密字符串
    SECRET_KEY = "SAKLDLASKJDLASDSAKNJDJK9U898AS8D8"
# 1.创app对象
app = Flask(__name__)
# 关联配置
app.config.from_object(Config)

#2.创建数据库对象
db = SQLAlchemy(app)

#3.创建迁移对象(创建一个默认文件夹--migrations)
#第一个参数是Flask的实例，第二个参数是Sqlalchemy数据库实例
migrate = Migrate(app,db)

#4.创建管理类
manager = Manager(app)

#manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
#5.通过管理类添加数据库迁移指令
# db 数据库迁移命令
manager.add_command('db',MigrateCommand)

"""
(必须掌握)   第一次执行相当于：db.create_all()
# 第一次数据库迁移初始化操作 产生一个migrations文件夹 （只需执行一次）
python3 demo2_migrate.py db init
python3 database_move_migrate.py db init

# 执行数据库迁移 生成一个对应版本  -m：注释   (只要模型类的结构发生改变每次都需要执行)
python3 demo2_migrate.py db migrate -m "messge"
python3 database_move_migrate.py db migrate -m '备注'

# 执行数据库版本的升级 才会真正在数据库创建表  (只要模型类的结构发生改变每次都需要执行)
python3 demo2_migrate.py db upgrade
python3 database_move_migrate.py db upgrade


（会copy）
# 查看历史版本
python3 demo2_migrate.py db history
pythoon3 database_move_migrate.py db history

# 回到低版本
python3 demo2_migrate.py db downgrade 版本号
python3 database_move_migrate.py db downgrade 版本号

# 回到高版本
python3 demo2_migrate.py db upgrade 版本号
python3 database_move_migrate.py db upgrade 版本号


"""

# 定义模型类  作者
class Author(db.Model):
    # 定义表名
    __tablename__ = 'author'
    # 创建id 列
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),unique=True)
    books = db.relationship('Book',backref = 'author')
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.Integer, unique=True)
    def __repr__(self):
        return "Author: %s  %s"%(self.id, self.name)

# 定义模型类  书名
class Book(db.Model):
    __tablename__  = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    def __repr__(self):
        return 'Book:%s  %s   %s'%(self.id, self.name, self.author_id)


if __name__ == '__main__':
    manager.run()