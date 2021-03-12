import re


# -------------正则化------------------

# 获取包含“爬虫”这个关键字的句子
# text_string = '文本最重要的来源无疑是网络。我们要把网络中的文本获取形成一个文本数据。利用一个爬虫抓取到网络中的信息。爬取策略有广度爬取和深度爬取。根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分。'
# regex = '爬虫'
# P_string = text_string.split('。') # 用句号分割
# for line in P_string:
#     if re.search(regex, line) is not None:
#         print(line)

# 匹配任意一个字符
# regex = '爬.'
# P_string = text_string.split('。') # 用句号分割
# for line in P_string:
#     if re.search(regex, line) is not None:
#         print(line)

# 匹配起始和结尾字符串
# regex = '^文本'
# P_string = text_string.split('。') # 用句号分割
# for line in P_string:
#     if re.search(regex, line) is not None:
#         print(line)


# 使用中括号匹配多个字符
# text_string = ['[重要的]今年第七号台风23日登陆广东沿海地区','上海发布车库销售监管通知：违规者暂停网签资格',
#                '[紧要的]中国对印连发强硬信息，印度急切需要结束对峙']
# regex = '^\[[重紧]..\]'
# for line in text_string:
#     if re.search(regex, line) is not None:
#         print(line)
#     else:
#         print('not match')

# 使用转义符
# if re.search(r"\\","I have one nee\dle") is not None:
#     print("match it")
# else:
#     print("not match")


# 抽取文本中的数字
# year_strings = []
# strings = ['War of 1812', 'There are 5280 feet to a mile','Happy New Year 2016!']
# for string in strings:
#     if re.search('[1-2][0-9]{3}', string):
#         year_strings.append(string)
#
# print(year_strings)


# 抽取所有的年份
# year_string = '2016 was a good year, but 2017 will be better!'
# years = re.findall('[2][0-9]{3}', year_string)
# print(years)

# -----------------------------------numpy------------------------------

import numpy as np
# 2.3.1 创建数组
# vector = np.array([1,2,3,4])
# print(vector)
# matrix = np.array([[1,'Tim'], [2, 'Joey'], [3, 'Johnny'], [4, 'Frank']])
# print(matrix)

# 2.3.2 获取Numpy的维度
# a = np.arange(15).reshape(3, 5)
# print(a)
# print(a.shape)      # 获取a的维度


# 2.3.3 获取本地数据

# 2.3.4 正确读取数据

# 2.3.5 Numpy数组索引
# matrix = np.array([[1,2,3], [20,30,40]])
# print(matrix[0,1])

# 2.3.6 切片
# matrix = np.array([
#     [5, 10, 15],
#     [20, 25, 30],
#     [35, 40, 45]
# ])
# print(f"{matrix[:, 1]}\n")
# print(f"{matrix[:, 0:2]}\n")
# print(f"{matrix[1:3, :]}\n")
# print(matrix[1:3, 0:2])

# 2.3.7 数组比较
# matrix = np.array([
#     [5, 10, 15],
#     [20, 25, 30],
#     [35, 40, 45]
# ])
# m = (matrix == 25)
# print(m)
#
# #---------------------
# second_column_25 = (matrix[:,1] == 25)
# print(second_column_25)
# print(matrix[second_column_25, :])

# 2.3.8 替代值
# vector = np.array([5,10,15,20])
# equal_to_ten_or_five = (vector == 10) | (vector == 5)
# vector[equal_to_ten_or_five] = 50
# print(vector)

# 2.3.9 数据类型转换
# vector = np.array(["1", "2", "3"])
# print(vector.astype(float))

# 2.3.10 统计
vector = np.array([5,10,15,20])
print(vector.sum())
matrix = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])
print(matrix.sum(axis=1))       # 行的和，以列的形式展开
print(matrix.sum(axis=0))       # 列的和，以行的形式展开
