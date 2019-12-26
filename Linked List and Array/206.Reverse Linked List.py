# _*_ coding:utf-8 _*_
#文件作者: 郑海明
#开发时间：2019/10/17 8:06
#文件名称：206.Reverse Linked List.py
#开发工具：PyCharm


import random

"""
反转一个单链表
"""
class single_node:
    def __init__(self, val):
        self.val = val
        self.next = None

class my_linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head == None

    # 遍历链表
    def travel_linked_list(self):
        cur = self.head
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")

    # 头部添加元素
    def add_at_head(self, val):
        node = single_node(val)
        node.next = self.head
        self.head = node
        self.length += 1

    # 尾部添加元素
    def add_at_tail(self, val):
        node = single_node(val)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.length += 1

    # 指定位置添加元素
    def add_by_index(self, index:int, val):
        index = 0 if not isinstance(index, int) else index
        # if index < 0 or index >= self.length - 1:
        #     raise IndexError("index out of linked list range!")
        if index <= 0:
            self.add_at_head(val)
        elif index >= self.length:
            self.add_at_tail(val)
        else:
            node = single_node(val)
            count_index = 0
            pre = self.head                 # 用于记录指定位置的前一个元素
            while count_index < (index -1):
                count_index += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node
            self.length += 1

    # 反转链表
    def reverse_linked_list(self):
        cur, pre = self.head, None           # return pre
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        self.head = pre
        # return pre

def main():
    link_list = my_linked_list()

    # link_list.add_at_head(11)
    # link_list.add_at_tail(22)
    # link_list.add_at_head(10)
    link_list.add_at_tail(11)
    link_list.add_at_tail(22)
    link_list.add_at_tail(33)
    link_list.add_at_tail(44)
    link_list.add_at_tail(55)
    link_list.add_at_tail(66)
    link_list.add_at_tail(77)
    # link_list.add_by_index(0,'string')
    link_list.travel_linked_list()

    link_list.reverse_linked_list()
    link_list.travel_linked_list()

    # print(link_list.length)




if __name__ == "__main__":
    main()