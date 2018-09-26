import base64
import os
from urllib import response

from flask import Flask
from flask import make_response
from flask import render_template
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):

    def __init__(self,map, *arge):
        super(RegexConverter, self).__init__(map)
        self.regex = arge[0]

app = Flask(__name__)
#2.将自定义的类关联到url_map.converters形成键值对
app.url_map.converters['re'] = RegexConverter

def generete():
    csrf_token = bytes.decode(base64.b64encode(os.urandom(48)))
@app.route('/')
def index():
    csrf_token = generete()
    response = make_response(render_template('temp_index.html', csrf_token=csrf_token))
    # 浏览器有同源策略，网站B是获取不到网站A的cookie的，所以就解决了跨站请求伪造的问题
    # response.set_cookies('csrf_token', csrf_token)    会报错
    return response


if __name__ == '__main__':
    app.run(host='0.0.0',port=9000, debug = True)