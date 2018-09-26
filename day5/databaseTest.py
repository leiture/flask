#coding=utf-8
import unittest
from author_book_model import *

#自定义测试类，setUp方法和tearDown方法会分别在测试前后执行。以test_开头的函数就是具体的测试代码。
class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/test0'
        self.app = app
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    #测试代码
    def test_append_data(self):
        au = Author(name='haha')
        bk = Book(name='python')
        db.session.add_all([au,bk])
        db.session.commit()
        author = Author.query.filter_by(name='haha').first()
        book = Book.query.filter_by(name='python').first()
        #断言数据存在
        self.assertIsNotNone(author)
        self.assertIsNotNone(book)

if __name__ == '__main__':
    unittest.main()