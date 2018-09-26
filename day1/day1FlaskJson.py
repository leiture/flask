from flask import Flask, jsonify
from flask import json
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

@app.route('/json')
def demo():
    '''json数据转换'''
    dict = {
        "name":"leipeng",
        "age":18,
        "gender":"man",
        "job":"life"
    }
    # 序列化 : python对象转换成json字符串
    json_str = json.dumps(dict)
    # return json_str
    # 反序列化：json字符串转换成python对象(list dict)
    list_dict = json.loads(json_str)


    # 1.python对象转换成json字符串
    # 2.指明返回的数据的类型：Content-Type: "application/json"
    # 3.将响应体数据包装成响应对象
    request = jsonify(dict)
    # < Response 71 bytes [200 OK] >
    request.headers["Content-Type"] = "application/json"
    return request

if __name__ == '__main__':
    app.run('0.0.0.0',debug = True)