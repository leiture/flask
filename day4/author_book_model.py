from flask import redirect
from flask import render_template,flash
from flask import request
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# 创建系统配置类
class Config(object):
    DEBUG = True
    # 连接数据库
    SQLALCHEMY_DATABASE_URI ='mysql://root:mysql@127.0.0.1:3306/test2'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

# 创建Flask实例
app = Flask(__name__)
app.secret_key ='shdfkjsdh13j21k3h12k3h1231'
# 系统配置关联
app.config.from_object(Config)
# 实例化SQLALchemy对象
db = SQLAlchemy(app)

# 定义模型类  作者
class Author(db.Model):
    # 定义表名
    __tablename__ = 'author'
    # 创建id 列
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),unique=True)
    books = db.relationship('Book',backref = 'author')
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

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        authors = Author.query.all()
        return render_template('temp1_bookDemo.html', authors = authors)

    if request.method =='POST':
        author_name = request.form.get('author')
        author_book = request.form.get('book')
        if not all([author_name,author_book]):
            flash('缺少参数')
            return redirect(url_for('index'))

        # 查询作者是否存在
        author = Author.query.filter(Author.name ==author_name).first()
        if author:
            # 判断当前作者是否有同名的书
            book = Book.query.filter(Book.name==author_book, Book.author_id == author.id).first()
            if book:
                flash('已经存在相同名称书籍。')
            else:
                # 将指定的书添加到作者下面
                try:
                    book = Book(name=book, author_id=author.id)
                    db.session.add(book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash('添加失败！')

        else:
            # 如果作者不存在
            # 添加作者
            author = Author(name = author_name)
            # 添加书籍
            book = Book(name = author_book)
            # 能book设置其对应的作者是什么
            # 那么在添加book的时候，ORM会去自己帮我们查询是否有对应的作者，如果没有，就直接添加
            book.author = author
            try:
                db.session.add(book)
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
                flash("添加失败")
        # 添加书籍和作者成功后，刷新页面
        return redirect(url_for('index'))

# 删除作者
@app.route('/delete_author')
def delete_author():
    try:
        aid = request.args.get('aid')
        # 通过aid找到对应的作者模型（判断是否存在模型）
        author = Author.query.get(aid)
    except Exception as e:
        print(e)
        return
    if not author:
        flash('作者不存在！')
        return render_template(url_for('index'))
    else:
        try:
            # 删除书籍
            Book.query.filter(Book.author_id == aid).delete()
            # 删除作者
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
    # 重定向
    return redirect(url_for('index'))

@app.route('/delete_book')
def delete_book():
    bid = request.args.get('bid')
    book = Book.query.get(bid)
    # 判断书籍存在
    if book:
        # 删除书籍
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
    else:
        flash('书籍不存在！')

    return redirect(url_for('index'))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    # 生成数据
    au1 = Author(name='王老二')
    au2 = Author(name='雷总')
    au3 = Author(name='Hide on bush')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()
    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()
    app.run()