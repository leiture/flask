from flask import Flask, render_template
from flask import request
from flask import url_for
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):

    def __init__(self,url_map,*args):
        super(RegexConverter, self).__init__(url_map)
        self.regex = args[0]

app =Flask(__name__)
# app.config['DEBUG'] = True
app.url_map.converters['re'] = RegexConverter

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/name/<re('[0-9]{6}'):use_name>")
def get_name(use_name):
    return 'hello %s'%use_name

@app.route('/user/<use_id>')
def use_id(use_id):
    return 'hello %d'%use_id

@app.route('/query_name')
def query_name():
    id  = request.args.get('id')
    return 'hello %s'%id

@app.route('/query_url')
def query_url():
    return url_for('query_name')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)