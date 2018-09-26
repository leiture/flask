#0.导入python自带单元测试类
import unittest

from flask import json

from login_test import app

#1.自定义单元测试类，继承unittest.TestCase
class LoginTest(unittest.TestCase):
    # 初始化方法
    # 该方法会首先执行，相当于做测试前的准备工作
    def setUp(self):
        # 相当于开启debug模式，精确定位被测试的代码的异常信息
        app.testing = True
        # 发送网络请求的客户端
        self.client = app.test_client()

        # 单元测试函数，注意：该函数必须以test_开头

    # 该方法会在测试代码执行完后执行，相当于做测试后的扫尾工作
    def tearDown(self):
        pass

        # 单元测试函数，注意：该函数必须以test_开头

    def test_empty_username_password(self):
        """测试用户名与密码为空的情况[当参数不全的话，返回errcode=-2]"""
        response = app.test_client().post('/login', data={})
        json_data = response.data.decode()
        json_dict = json.loads(json_data)

        self.assertIn('errcode', json_dict, '数据格式返回错误')
        self.assertEqual(json_dict['errcode'], -2, '状态码返回错误')

        # TODO 测试用户名为空的情况
        # TODO 测试密码为空的情况

    def test_error_username_password(self):
        """测试用户名和密码错误的情况[当登录名和密码错误的时候，返回 errcode = -1]"""
        response = app.test_client().post('/login', data={"username": "aaaaa", "password": "12343"})
        json_data = response.data.decode()
        json_dict = json.loads(json_data)
        self.assertIn('errcode', json_dict, '数据格式返回错误')
        self.assertEqual(json_dict['errcode'], -1, '状态码返回错误')

        # TODO 测试用户名错误的情况
        # TODO 测试密码错误的情况

if __name__ == '__main__':
    unittest.main()