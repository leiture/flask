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
    my_list = [
        {
            "id": 1,
            "value": "我爱工作"
        },
        {
            "id": 2,
            "value": "工作使人快乐"
        },
        {
            "id": 3,
            "value": "沉迷于工作无法自拔"
        },
        {
            "id": 4,
            "value": "日渐消瘦"
        },
        {
            "id": 5,
            "value": "以梦为马，越骑越傻"
        }
    ]
    return render_template('day2controlblock.html', list = my_list)

if __name__ == '__main__':
    app.run(host='0.0.0',debug = True)