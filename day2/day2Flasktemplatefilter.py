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
    list = [1, 5, 2, 4, 3]
    html_str = "<h1>我是标题</h1>"
    goods_list = [
        {
            "goods_name": "西瓜",
            "price": 10
        },
        {
            "goods_name": "荔枝",
            "price": 8
        }
    ]
    return render_template('day2templatefilter.html',
                           list=list,
                           html_str=html_str,
                           goods_list=goods_list
                           )

if __name__ == '__main__':
    app.run(host='0.0.0',debug = True)