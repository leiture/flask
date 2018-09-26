from flask import Flask
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

# 第一次请求之前调用该视图函数(只会调用一次)
# 应用场景: 初始化操作
@app.before_first_request
def before_first_request():
    print('before_first_request')
    return 'before_first_request'

# 每次请求之前都会调用该视图函数(调用多次)
# 应用场景：ip处理(封ip)
@app.before_request
def before_request():
    print("before_request")
    # return 'before_request'

# 每次请求之后会调用该视图函数(调用多次)
# 应用场景：可以拦截对响应对象进行统一处理
@app.after_request
def after_request(response):
    # 拦截处理
    # response.headers["Content-Type"] = "application/json"
    # response.set_cookie
    print('after_request')
    return response

# 每次请求结束之后会调用该视图函数(调用多次)
# 每次会传入error  如果请求没有错误 error为空
# 应用场景：异常处理
@app.teardown_request
def teardowm_request(error):
    print(error)
    print('teardowm_request')

if __name__ == '__main__':
    app.run('0.0.0.0',debug = True)