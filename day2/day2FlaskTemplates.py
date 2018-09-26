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
    my_int = 18
    my_str = "laowang"
    my_list = [1, 4, 2, 3, 5]
    my_dict = {
        "name": "harden",
        "age": 28
    }
    # 使用render_template渲染模板
    # 参数1：模板名称  参数n: 需要传入到模板里面的参数，以键值对的形式往后排
    return render_template('index.html',
                           my_int=my_int,
                           my_list=my_list,
                           my_string=my_str,
                           my_dict=my_dict)


if __name__ == '__main__':
    app.run('0.0.0',debug = True)