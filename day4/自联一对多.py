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

class Comment(db.Model):
    """评论"""
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    # 评论内容
    content = db.Column(db.Text, nullable=False)
    # 父评论id
    parent_id = db.Column(db.Integer, db.ForeignKey("comments.id"))
    # 父评论(也是评论模型)
    parent = db.relationship("Comment", remote_side=[id],
                             backref=db.backref('childs', lazy='dynamic'))

# 测试代码
if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    com1 = Comment(content='我是主评论1')
    com2 = Comment(content='我是主评论2')
    com11 = Comment(content='我是回复主评论1的子评论1')
    com11.parent = com1
    com12 = Comment(content='我是回复主评论1的子评论2')
    com12.parent = com1

    db.session.add_all([com1, com2, com11, com12])
    db.session.commit()
    app.run(debug=True)