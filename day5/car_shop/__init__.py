# 专门在init文件做导入工作，视图函数的业务逻辑代码放到views.py
from flask import Blueprint
# 创建蓝图对象
car_shopping = Blueprint('car_shopping',
                         __name__,
                         static_folder='static',

                         template_folder='templates',
                         url_prefix='/car_shopping')

#2.延迟导入 （切记一定要导入views文件，不然整个包就发现不了里面的视图函数，没法注册路由）
from .views import *