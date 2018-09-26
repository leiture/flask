from flask import Flask
from flask import make_response
from flask import request
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):

    def __init__(self,map, *arge):
        super(RegexConverter, self).__init__(map)
        self.regex = arge[0]

app = Flask(__name__)
#2.将自定义的类关联到url_map.converters形成键值对
app.url_map.converters['re'] = RegexConverter

@app.route('/')
def index():
    return 'hello world!'

@app.route('/set_cookie')
def set_cookie():
    # 1,建立连接
    response = make_response('set cookie success!')
    # 2.使用响应对象中的set_cookie方法设置用户信息(键值对)
    # 参数1：key  参数2：value 参数3：max_age代表过期时长
    response.set_cookie('username','leipeng',max_age=3600)
    response.set_cookie('password','123456',max_age=3600)
    return response

@app.route('/get_cookie')
def get_cookie():
    """再次请求首页的时候获取cookie中的用户信息"""
    user_name = request.cookies.get('username','')
    password = request.cookies.get('password', '')
    return "%s---->>%s"%(user_name, password)

@app.route('/out_cookie')
def out_cookie():
    """退出登录删除cookie中保存的用户数据"""
    # 1.构建响应对象
    response = make_response('out cookie success!')
    # 2.借助响应对象中的delete_cookie方法删除cookie中的数据
    response.delete_cookie('username')
    response.delete_cookie('password')
    return response

if __name__ == '__main__':
    app.run('0.0.0.0',debug = True)