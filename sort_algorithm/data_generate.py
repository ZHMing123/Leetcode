# _*_ coding:utf-8 _*_
#文件作者: ZHMing123
#开发时间：2019/11/16 11:07
#文件名称：data_generate.py
#开发工具：PyCharm


import random
import time

def data_generate(range_number):
    data = []
    for i in range(0, 30000):
        # yield random.randint(0, range_number)
        data.append(random.randint(0, range_number))
    return data

start = time.time()
data = data_generate(10000)
with open('data.txt', 'w') as f:
    index = 0
    for i in data:
        if index % 10 == 0 and index != 0:
            f.write("\n")
        f.write(str(i) + "\t")
        index += 1
        # print(i)
end = time.time()
print("cost time:{}".format(end - start))

read_start = time.time()
input_data = []
with open('data.txt', 'r') as f:
    for line in f.readlines():
        data_line = line.strip().split("\t")
        for data in data_line:
            input_data.append(int(data))
read_end = time.time()
print(input_data)
print(len(input_data))
print("cost time:{}".format(read_end - read_start))