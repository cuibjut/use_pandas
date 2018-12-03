#!coding=UTF_8

import codecs


dict1 = {'1': ["a", "b", "c"],
             '2': ["b", "c", "d"]}
for key, values in dict1.items():
    with codecs.open("sample.csv", "w", 'gbk') as f2:
            value = ("\n").join(values) + "\n"
            f2.write(value.encode("gbk", 'ignore').decode("gbk", "ignore"))