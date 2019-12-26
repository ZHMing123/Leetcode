# _*_ coding:utf-8 _*_
#文件作者: 郑海明
#开发时间：2019/10/17 22:37
#文件名称：225.Queue achieve Stack.py
#开发工具：PyCharm


import random
from queue import PriorityQueue

"""
python用队列实现栈

"""
k = 5
priority_queue = PriorityQueue(maxsize=5)
priority_queue.put(5)
priority_queue.put(3)
priority_queue.put(1)
priority_queue.put(-1)
priority_queue.put(6)
# priority_queue.put(7, timeout=2)
# 非阻塞
priority_queue.put(7, block=False)
print(priority_queue.get())
print(priority_queue.get())
print(priority_queue.get())
print(priority_queue.get())
print(priority_queue.get())
print(priority_queue.get())
