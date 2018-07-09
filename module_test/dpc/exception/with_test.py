with open('../imooc.ini') as f:
    for line in f.readlines():
        print line
print "file is closed ?", f.closed  #利用with语句会自动的关闭文件


# with 语句实际上是进行了一个上下文的管理 上下文管理器必须有 __enter__()  和 __exit()__