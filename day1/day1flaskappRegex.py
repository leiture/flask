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

@app.route('/name/<re(r"\\w{3}"):name>')
def get_name(name):
    return 'hello %s'%name

if __name__ == '__main__':
    app.run('0.0.0.0',port=9999,debug = True)