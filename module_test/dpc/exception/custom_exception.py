# -*- coding:utf-8 -*-
class CustomError(Exception):
    def __init__(self, info):
        # Exception.__init__(self)   为何注释掉不执行这句话也可以进行初始化 ？ 派生类的初始化过程?
        self.info = info

    def __str__(self):
        return "CustomError :%s" % self.info


if __name__ == '__main__':
    try:
        raise CustomError("用户自定义的异常")
    except Exception as c:
        print type(c)
        print c
        print id(c)
