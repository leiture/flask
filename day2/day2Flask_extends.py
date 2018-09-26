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
    return 'hello world!'

@app.route('/parent')
def parent():
    return render_template('day2parent.html')

@app.route('/child')
def child():
    return render_template('day2child.html')

if __name__ == '__main__':
    app.run(host='0.0.0',debug = True)