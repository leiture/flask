from flask import Flask, jsonify
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

@app.route('/login', methods=['POST', 'GET'])
def login():
    username = request.form.get('username','')
    password = request.form.get('password','')
    if not all([username,password]):
        result = {
            'errcode':-2,
            'errmsg':'parms error'
        }
        return jsonify(result)
    a = 1/0
    # 如果账号密码正确
    # 3. 判断账号密码是否正确
    if username=='leipeng' and password=='python':
        result = {
            'errcode':0,
            'errmsg':'successfully!'
        }
        return jsonify(result)
    else:
        result = {
            'errcode':-1,
            'errmsg':'wrong username or password'
        }
        return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0',debug = True)