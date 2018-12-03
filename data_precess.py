#!coding=UTF_8

import pandas as pd

# 1.导入数据
# 读文件(不是csv文件) 默认第一列不作为索引值:header=None， sep="\t"
# df1 = pd.read_table("sample1.txt", header=None, sep="\t")

# 读文件（csv文件）默认第一列不作为索引值： header=None
# df2 = pd.read_csv("sample2.csv", header=None)

# 使用字典创建dataFrame
df3 = pd.DataFrame({'total_bill': [16.99, 10.34, 23.68, 23.68, 24.59],
                    'tip': [1.01, 1.66, 3.50, 3.31, 3.61],
                    'sex': ['Female', 'Male', 'Male', 'Male', 'Female']})
"""
df3格式如图：
   total_bill   tip     sex
0       16.99  1.01  Female
1       10.34  1.66    Male
2       23.68  3.50    Male
3       23.68  3.31    Male
4       24.59  3.61  Female
"""

# 2.导出数据
df3.to_csv("sample3.csv")


# 3.查看检查数据
print(df3)
print(df3.head(3))  # 查看前3行
print(df3.tail(3))  # 查看后3行
print(df3.shape)  # 查看行数和列数 tuple (5, 3)
print(df3.info())  # 查看索引，数据类型和内存信息
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
total_bill    5 non-null float64     可以看到每一列有多少空值，每一类的数据类型
tip           5 non-null float64      每一列的columns值
sex           5 non-null object
dtypes: float64(2), object(1)
memory usage: 200.0+ bytes        
None
RangeIndex(start=0, stop=5, step=1)   #index值的范围
"""


print(df3.index)  # 返回行的index值
# RangeIndex(start=0, stop=5, step=1)

print(df3.values)  # 返回一个二维数组的值
""""
[[16.99 1.01 'Female']
 [10.34 1.66 'Male']
 [23.68 3.5 'Male']
 [23.68 3.31 'Male']
 [24.59 3.61 'Female']]
"""

print(df3.columns)  # 返回一个列的index的Series
# Index(['total_bill', 'tip', 'sex'], dtype='object')

print(df3.describe())  # 查看数值型列的汇总信息
"""
       total_bill       tip
count    5.000000  5.000000
mean    19.856000  2.618000
std      6.132392  1.198361
min     10.340000  1.010000
25%     16.990000  1.660000
50%     23.680000  3.310000
75%     23.680000  3.500000
max     24.590000  3.610000
"""

# 4.数据选取
"""
取列的方法：
df[col]：根据列名，并以Series的形式返回列   
df[[col1, col2]]：列名，以DataFrame形式返回多列

取行的方法：
df.loc[]:基于列的label，可选取特定的行
df.iloc[]:列的index
df.loc[0,0]：返回第一列的第一个元素
df[col:col+1] 取第col行
"""

# 取列
print("------取列-------")
print(df3['total_bill'])
print(df3[['total_bill']])
print(df3.loc[1])  # 取第一列
# 取行
print("-------取行------")
print(df3[0:1])  # 取第0行元素的值
print(df3.loc[1: 3, ['total_bill', 'tip']])  # 取1-3行的某列的值
print(df3.loc[2, :])   # 第三行的所有值，返回一个Series
# 取单个值
print("-------取单个值------")
print(df3.loc[2, 'sex'])  # 第3行的列属性为'sex'的值
print(df3.at[3, 'tip'])
# 将DataFrame中的所有值转化为而为数组的表示
print(df3.values)  # 没有括号

# 数据统计
print(df3.describe())  # 查看数据值列的汇总统计
print(df3.mean())  # 查看所有列的均值
print(df3.corr())  # 返回列于列的相关系数
print(df3.count())  # 返回每个列的非空值个数
print(df3.max())  # 返回每一列的最大值
print(df3.min())  # 返回每一列的最小值
print(df3.median())  # 返回每一列的中位数
print(df3.std())  # 返回每一列的标准差
print(df3['total_bill'].quantile(0.25))  # 返回分位数







