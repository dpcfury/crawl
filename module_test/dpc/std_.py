# -*- coding:utf-8 -*-
import sys
#
# a =raw_input(':')
# print a

print sys.stdin.fileno()
print sys.stdout.fileno()
print sys.stdout.mode  # 标准输出文件只写 标准输入文件是只读
sys.stderr.write("wolegequ")
print sys.stderr.mode
print sys.stderr.fileno()


