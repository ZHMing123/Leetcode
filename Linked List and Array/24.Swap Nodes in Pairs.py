# _*_ coding:utf-8 _*_
#文件作者: 郑海明
#开发时间：2019/10/17 8:42
#文件名称：24.Swap Nodes in Pairs.py
#开发工具：PyCharm

import random

"""
反转相邻的两个节点
input：1 -> 2 -> 3 -> 4 -> 5
output: 2 -> 1 -> 4 -> 3 -> 5
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

    # 反转相邻的两个节点
    def swap_node_in_pairs(self):
        # if self.length < 2:
        #     return
        res = single_node(0)
        pre, pre.next = res, self.head
        # print(pre.next)
        # print(res.next)
        # pre移动，边界条件为还剩至少两个非空节点
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next

            # 此时，pre is res, pre.next(即res.next) = head
            # print(pre.next)
            # print(res.next)
            # print('*'*30)

            # 此时，pre is res, pre.next(即res.next) = b
            pre.next, a.next, b.next = b, b.next, a

            # pre = pre.next.next后，pre is not res
            # pre之后的改变不影响res, 且之后res.next一直指向节点第一轮的b
            pre = pre.next.next                 # 即pre = a (新的a)

        self.head = res.next
        # print(res.next)
        # return res.next

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

    link_list.swap_node_in_pairs()
    link_list.travel_linked_list()

    # link_list.reverse_linked_list()
    # link_list.travel_linked_list()

    # print(link_list.length)
    # d = single_node(0)
    # print(d)
    # print(d.next)
    # # print(d1)
    # # print(d)
    # # print(d1.next)
    # # print(d.next)
    # # d.next = 0
    # # print(d.next)
    # # p = d
    # # print(p)
    # # print(p.next)
    # head = 0
    # pre, pre.next = d, head
    # print(d)
    # print(d.next)
    # print(pre)
    # print(pre.next)


if __name__ == "__main__":
    main()