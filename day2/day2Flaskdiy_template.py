from flask import Flask
from flask import render_template
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

#1.自定义列表反转的函数
@app.template_filter('list_reverse')
def do_myself_template(list):
    list.reverse()
    return list
#2.通过add_template_filter方法添加自定义函数到jinja2模板过滤器中
# 参数1：函数名称 参数2： 过滤器名称
# app.add_template_filter(do_myself_template,'list_reverse')

@app.route('/diy')
def div():
    list = [1,22,314,14151,55,51]
    return render_template('day2diy.html', list=list)

if __name__ == '__main__':
    app.run(host='0.0.0',debug = True)