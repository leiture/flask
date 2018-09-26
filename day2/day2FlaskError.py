from flask import Flask
from flask import abort
from flask import redirect
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
    a= 2/0
    # 主动产生一个异常  状态码：必须是http标准状态码
    abort(404)
    return 'hello world!'

# 例如统一处理状态码为500的错误给用户友好的提示：
# 使用app.errorhandler捕获错误状态码
@app.errorhandler(404)
def error(e):
    print(e)
    return redirect('https://www.baidu.com/search/error.html')

# 使用app.errorhandler捕获异常信息
@app.errorhandler(ZeroDivisionError)
def zero_division(e):
    print(e)
    return 'division by zero'

if __name__ == '__main__':
    app.run('0.0.0.0',debug = True)