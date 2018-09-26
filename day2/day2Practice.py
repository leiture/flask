from flask import Flask
from flask import current_app
from flask import g
from flask import make_response
from flask import session
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
    print(current_app.name)
    print(g.name)
    return 'hello world! '

@app.route('/cookie')
def set_cookie():
    resp = make_response('this is to set cookie')
    resp.set_cookie('username', 'itcast',max_age=100)
    return resp

@app.route('/set_session')
def set_session():
    session['username'] = 'itcast'
    return 'set_session successfully'

@app.route('/get_session')
def get_session():
    return session.get('username')

@app.errorhandler(500)
def internal_server_error(e):
    return '服务器搬家了！'

@app.errorhandler(ZeroDivisionError)
def zero_division_error():
    return '0不能为除数！'

if __name__ == '__main__':
    app.run('0.0.0.0',debug = True)