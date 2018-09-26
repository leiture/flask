from flask import Flask,g
from flask import render_template
from flask import session
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):

    def __init__(self,map, *arge):
        super(RegexConverter, self).__init__(map)
        self.regex = arge[0]

app = Flask(__name__)
#2.将自定义的类关联到url_map.converters形成键值对
app.url_map.converters['re'] = RegexConverter

@app.route('/index')
def index():
    """主页"""
    return render_template('index.html')

@app.route('/detail')
def detail():
    """个人页面"""
    return render_template('detail.html')

@app.route('/specail')
def specail():
    session.name = 'leipeng'
    g.user = 'wang'
    return render_template('specail.html')


if __name__ == '__main__':
    app.run(host='0.0.0',debug = True)