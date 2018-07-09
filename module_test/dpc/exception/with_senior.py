# -*- coding:utf-8 -*-

'''
上下文管理器是可以在with语句中使用，拥有__enter__和__exit__方法的对象。
个人理解 with语句简化了 try finally的最后资源清理工作
'''

class MyContext(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print "__Enter__"
        return self  # enter 如何需要返回这个对象

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "Error:", exc_type, "Info:", exc_val
        print "__Exit__"
        # return True  return True的情况下异常不会传播


    def do_self(self):
        print "do_self"
        print a  # 设置打印一个undefined的变量a 查看执行情况

if __name__ == '__main__':
    with MyContext("dpc") as f:
        print f.name
        f.do_self()

