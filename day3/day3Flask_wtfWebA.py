from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.routing import BaseConverter
# from flask.ext.wtf import CSRFProtect
# CSRFProtect(app)

class RegexConverter(BaseConverter):

    def __init__(self,map, *arge):
        super(RegexConverter, self).__init__(map)
        self.regex = arge[0]

app = Flask(__name__)
#2.将自定义的类关联到url_map.converters形成键值对
app.url_map.converters['re'] = RegexConverter
app.secret_key='lksdjfoeii@#$%OJJHJLHJLH'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # 获取表单的数据
        username = request.form.get('username')
        password = request.form.get('password')
        if not all([username, password]):
            print('参数错误！')
        else:
            print(username, password)
            if username=='leipeng' and password =='123':
                # 状态保存，设置用户名到COOKIE中表示登陆成功
                response = redirect(url_for('transfer'))
                response.set_cookie('username', username)
                return response
            else:
                print('密码错误')
    return render_template('temp_login.html')

@app.route('/transfer', methods=['POST', 'GET'])
def transfer():
    # 从cookies中获取用户名
    username = request.cookies.get('username', None)
    # 如果没有取到，代表没有登陆
    if not username:
        return redirect(url_for('index'))

    if request.method == "POST":
        to_account = request.form.get('to_account')
        money = request.form.get('money')
        print('假装执行操作，将当前登陆用户的钱转到制定账户')
        return '转帐%s元到%s成功。'%(money, to_account)

    # 渲染转换页面
    response = make_response(render_template('temp_transfer.html'))
    return response

if __name__ == '__main__':
    app.run(host='0.0.0',port= 8000,debug = True)