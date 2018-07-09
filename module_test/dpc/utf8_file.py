# -*- coding:utf-8 -*-
import codecs
f =codecs.open('imooc.data','w','utf-8')
print f.encoding
f.write(u"你们这些唇笔,到底怎么想的")  # 没有u会显示转码错误 因为encode是吧Unicode转string，而不是string =》string 所以会先decode 然而中文字符串不是正确的ascii码
f.close()