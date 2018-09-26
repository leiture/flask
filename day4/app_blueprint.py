from flask import Blueprint

# 创建蓝图对象
from flask import render_template
from flask import url_for
# static_folder=None,
# static_url_path=None, template_folder=None,
# url_prefix=None, subdomain=None, url_defaults=None
cart_bp = Blueprint('cart_bp', __name__,static_folder='static_admin',template_folder='templates_admin')

#2.蓝图的使用
@cart_bp.route('/')
def index():

    return render_template('blueprint.html')

@cart_bp.route('/user')
def user():
    return 'user blueprint!'
