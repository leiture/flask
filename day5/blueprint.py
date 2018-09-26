from flask import Flask
from werkzeug.routing import BaseConverter
from car_shop import car_shopping

class RegexConverter(BaseConverter):

    def __init__(self,map, *arge):
        super(RegexConverter, self).__init__(map)
        self.regex = arge[0]

app = Flask(__name__)
#2.将自定义的类关联到url_map.converters形成键值对
app.url_map.converters['re'] = RegexConverter

#4.注册蓝图
app.register_blueprint(car_shopping)

@app.route('/')
def index():
    return 'hello day5blueprint!'


if __name__ == '__main__':
    app.run(host='0.0.0',debug = True)