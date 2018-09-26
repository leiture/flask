from flask import Flask
from flask import session
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):

    def __init__(self,map, *arge):
        super(RegexConverter, self).__init__(map)
        self.regex = arge[0]


app = Flask(__name__)
#2.将自定义的类关联到url_map.converters形成键值对
app.url_map.converters['re'] = RegexConverter
# 设置加密字符串：flask会将这个混淆字符串和session进行加密
app.secret_key = 'sadfaskfjalsdj'
# app.config['SECRET_KEY'] = 'WUEH02EHRW*&6JBJSDHJFSH'

@app.route('/')
def index():
    return 'hello world!'

@app.route('/set_session')
def set_session():
    """登录成功使用session保存用户登录成功的数据"""
    # session是将用户数据保存到服务器的内存中-->项目中会将session的存储调整到redis数据库
    session['user_name'] = 'leipeng'
    session['password'] = '123123'
    return 'set session success!'

@app.route('/get_session')
def get_session():
    """访问首页使用session获取用户登录信息"""
    user_name = session.get('user_name', '')
    password = session.get('password', ' ')
    return '%s--->>>%s'%(user_name, password)

@app.route('/out_session')
def out_session():
    session.pop('user_name', ' ')
    session.pop('password', '')
    return 'delete session success!'

if __name__ == '__main__':
    app.run('0.0.0.0',debug = True)