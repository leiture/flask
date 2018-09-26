from redis import *

def redis_set_kv():
    """使用redis设置键值对数据"""
    # 使用默认值的方式创建redis对象
    # decode_responses=True 将二进制的数据decode成字符串
    sr = StrictRedis(host='localhost',port=6379,db=0,decode_responses=True)
    sr.set('name','lei')
    print(sr.get('name'))

if __name__ == '__main__':
    redis_set_kv()

