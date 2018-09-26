from flask import Flask
from werkzeug.routing import BaseConverter
from flask_script import Manager

class RegexConverter(BaseConverter):

    def __init__(self,map, *arge):
        super(RegexConverter, self).__init__(map)
        self.regex = arge[0]

app = Flask(__name__)
#2.将自定义的类关联到url_map.converters形成键值对
app.url_map.converters['re'] = RegexConverter
#2.创建管理对象 将app交给manager管理
manger = Manager(app)
manger.add_command('')

"""
命令：
# 查看帮助信息
python3 demo5_script.py runserver --help
# 动态指明ip和端口的形式运行项目
python3 demo5_script.py runserver -h 127.0.0.1 -p 8001 -d
python3 项目名称 runserver -h ip地址 -p 端口号 -d  #(开启debug模式)
"""

@app.route('/index')
def index():
    return 'hello world!'

if __name__ == '__main__':
    # app.run('0.0.0.0',debug = True)
    manger.run()