import pandas

def readFile():
    print('正在初始化数据...')
    data = pandas.read_excel('C:/Users/admin/Desktop/topic.xlsx')
    print('初始化数据完成...')
    return data
