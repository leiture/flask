from flask import Flask,g
from flask import current_app
from flask import request
from flask import session
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):

    def __init__(self,map, *arge):
        super(RegexConverter, self).__init__(map)
        self.regex = arge[0]

app = Flask(__name__)
#2.将自定义的类关联到url_map.converters形成键值对
app.url_map.converters['re'] = RegexConverter

app.secret_key = 'asjkdfhkjaha%$J#^#J%#*&%#'

@app.route('/')
def index():
    return 'hello world!'

@app.route('/request_context')
def request_context():
    url = request.url
    methods = request.method
    session['password'] = '123123'
    return '%s-->>%s------>>>%s'%(url,methods, session.get('password', ''))

@app.route('/application_context')
def application():
    # 应用上下文(current_app g)
    # 用于存储应用程序中的变量
    debug = current_app.config.get('DEBUG',"")
    g.name = 'asd'
    return '%s--->>%s'%(debug, g.name)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)