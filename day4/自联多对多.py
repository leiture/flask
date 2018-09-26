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
tb_user_follows = db.Table(
    "tb_user_follows",
    db.Column('follower_id', db.Integer, db.ForeignKey('info_user.id'), primary_key=True),  # 粉丝id
    db.Column('followed_id', db.Integer, db.ForeignKey('info_user.id'), primary_key=True)  # 被关注人的id
)

class User(db.Model):
    """用户表"""
    __tablename__ = "info_user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)

    # 用户所有的粉丝，添加了反向引用followed，代表用户都关注了哪些人
    followers = db.relationship('User',
                                secondary=tb_user_follows,
                                primaryjoin=id == tb_user_follows.c.followed_id,
                                secondaryjoin=id == tb_user_follows.c.follower_id,
                                backref=db.backref('followed', lazy='dynamic'),
                                lazy='dynamic')


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    user1 = User(name='lei')
    user2 = User(name='wang')
    user3 = User(name='faker')
    user2.followers = [user1,user3]
    user1.followers = [user2,user3]
    user3.followers = [user1,user2]

    db.session.add_all([user1,user2,user3])
    db.session.commit()
    app.run()