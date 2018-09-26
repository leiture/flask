from flask import Flask
from flask import render_template
from flask import url_for
from werkzeug.routing import BaseConverter
# 导入蓝图对象
from app_blueprint import cart_bp
class RegexConverter(BaseConverter):

    def __init__(self,map, *arge):
        super(RegexConverter, self).__init__(map)
        self.regex = arge[0]

app = Flask(__name__)
# 蓝图的作用：分模块开发
#4.注册蓝图到app中
# 当我们在应用对象上注册一个蓝图时，可以指定一个url_prefix关键字参数（这个参数默认是/）
app.register_blueprint(cart_bp, url_prefix = '/cart_bp')
# ImportError: cannot import name 'cart_info'
# 循环导入了 解决方案: 一边让步 延迟导入
#2.将自定义的类关联到url_map.converters形成键值对
app.url_map.converters['re'] = RegexConverter

@app.route('/')
def index():
    return render_template('temp1_bookDemo.html')
@app.route('/user')
def user():
    return 'user html'

if __name__ == '__main__':

    app.run(host='0.0.0',debug = True)