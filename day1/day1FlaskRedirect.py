from flask import Flask
from flask import redirect
from flask import url_for
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):

    def __init__(self,map, *arge):
        super(RegexConverter, self).__init__(map)
        self.regex = arge[0]

app = Flask(__name__)
#2.将自定义的类关联到url_map.converters形成键值对
app.url_map.converters['re'] = RegexConverter

@app.route('/')
def hello_world():
    return 'hello !!','999 clearlove'

@app.route('/index/<use_id>')
def index(use_id):
    return 'hello world! %s'%use_id

@app.route('/demo1')
def demo1():
    # 使用redirect函数完成重定向 参数：url
    return redirect('http://www.itheima.com')

@app.route('/demo2')
def demo2():
    """重定向到hello_world的根路径 /"""
    # url_for反向解析函数： 将函数名称传入(app.url_map)返回这个视图函数对应的url
    return redirect(url_for('index', use_id=777))

if __name__ == '__main__':
    app.run('0.0.0.0',debug = True)