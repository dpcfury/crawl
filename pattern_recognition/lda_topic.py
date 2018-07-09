import os
'''
通过gensim提供的LDA模型实现，提取package为单位的topic主题分布
根据CCP概念耦合程度再进行聚类操作
1. 文本预处理（分词 ，切词，去大小写，词干化，去停用词）
'''
#读取文件，创建map
files = os.listdir('corpus')
documents = {}
for s in files:
    with open(os.path.join('corpus', s)) as f:
        documents[s] = f.read()

#遍历字典，进行预处理和索引
for temp in documents.keys():
    print(temp + "\n" + documents[temp])

