# _*_ coding:utf-8 _*_
#文件作者: 郑海明
#开发时间：2019/10/17 20:47
#文件名称：232.Stack achieve Queue.py
#开发工具：PyCharm


import random

"""
python用栈实现队列

思路：用两个栈stack1（输入栈）和stack2（输出栈）来实现队列   
    1、push操作 -> 所有元素都从stack1入栈 
    2、pop、peek操作 -> 遇到pop和peek，先将stack1中的所有元素出栈，
                       并压入stack2中，再stack2.pop()或者stack2[-1]
           
"""
class my_queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # 入队
    def push(self, val):
        self.stack1.append(val)

    # 出队
    def pop(self):
        if self.is_empty():
            print("queue is empty!")
            return None
        # 将stack1中的所有元素出栈，并压入stack2中
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()

        # 将stack2中的所有元素重新压回stack1中
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return  res

    # 返回队首元素
    def peek(self):
        if self.is_empty():
            print("queue is empty!")
            return None
        return self.stack1[0]

    def is_empty(self):
        return not self.stack1

    # 出队
    def pop_method(self):
        if self.is_empty_method():
            print("queue is empty!")
            return None

        # stack2为空
        if not self.stack2:
            # 将stack1中的所有元素出栈，并压入stack2中
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        res = self.stack2.pop()

        # # 将stack2中的所有元素重新压回stack1中
        # while self.stack2:
        #     self.stack1.append(self.stack2.pop())

        return res

    # 返回队首元素
    def peek_method(self):
        if self.is_empty_method():
            print("queue is empty!")
            return None

        # stack2为空
        if not self.stack2:
            # 将stack1中的所有元素出栈，并压入stack2中
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        res =  self.stack2[-1]
        return res

    def is_empty_method(self):
        return not (self.stack1 or self.stack2)

def main():
    queue = my_queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    queue.push(6)

    print(queue.stack1)
    print(queue.stack2)
    print('*' * 30)

    # print(queue.peek())
    # print(queue.pop())
    # print(queue.peek())
    print(queue.peek_method())
    print(queue.pop_method())
    print(queue.peek_method())
    print(queue.stack1)
    print(queue.stack2)
    print('*'*30)

    queue.push(7)
    queue.push(8)
    print(queue.stack1)
    print(queue.stack2)
    print('*' * 30)

    print(queue.peek_method())
    print(queue.pop_method())
    print(queue.peek_method())
    print(queue.stack1)
    print(queue.stack2)


if __name__ == '__main__':
    main()
