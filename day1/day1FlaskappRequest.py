from flask import Flask
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

"""提取get请求问号后面携带的键值对参数"""
    # 使用request.method获取请求方式 注意：GET需要大写
# http://0.0.0.0:5000/get?name=leipeng&gender=man
@app.route('/get')
def get():
    if request.method=='GET':
        # 方法：request.args.get('key', '')
        name = request.args.get('name','')
        gender = request.args.get('gender','')
        return '%s--->%s'%(name,gender)
    else:
        return 'you should use GET<method>'

# http://0.0.0.0:5000/post
@app.route('/post',methods=['POST'])
def post():
    """获取post请求体里面携带的参数"""
    # 方法: request.form.get('key', '')
    if request.method == 'POST':
        get_name = request.form.get('name', '')
        get_gender = request.form.get('gender', '')
        return '%s>%s'%(get_name,get_gender)
    else:
        return 'method not POST!'


#0.0.0.0:5000/file
@app.route('/file', methods=['POST'])
def file():
    """传一张图片"""
    # 方法：request.files.get('key', '')
    if request.method == 'POST':
        file = request.files.get('pic', '')
        file.save('static/1.jpg')
        return 'upload successlly!'
    else:
        return 'error!'



if __name__ == '__main__':
    app.run('0.0.0.0',debug = True)