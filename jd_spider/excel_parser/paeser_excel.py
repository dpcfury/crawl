# -*- coding:utf-8 -*-
import xlrd

if __name__ == "__main__":
    # 预备读excel并将其中的url逐个塞入new_urls集合中进行初始化
    # 打开excel 文件
    data = xlrd.open_workbook('record.xls')
    # 通过名称获取工作表
    table = data.sheet_by_index(0)
    # 获取表格的行数和列数
    nrows = table.nrows

    # 从第二行开始讲每行的url读取出来
    print "正在从excel中提取用户购买记录.........."
    count = 0
    f = open('record.data', 'w')
    for i in range(1, nrows):
        row_values = table.row_values(i)
        pid = row_values[0].encode("utf-8")
        uid = row_values[7].encode("utf-8")
        print "%s , %s" % (uid, pid)
        f.write("%s::%s\n" % (uid, pid))
        count += 1
    f.close()
    print "一共读取了%d条的用户购买记录" % count

