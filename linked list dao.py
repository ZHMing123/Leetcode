# _*_ coding:utf-8 _*_
#文件作者: 郑海明
#开发时间：2019/10/16 17:29
#文件名称：linked list dao.py
#开发工具：PyCharm

import random

"""
python创建链表
"""


# 单链表的节点
class single_node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


# 单链表
class my_link_list(object):

    def __init__(self):
        self.head = None
        self.length = 0

    # 判断链表是否为空
    def is_empty(self):
        return self.head == None

    # 链表长度
    def link_list_length(self):
        cur = self.head
        count = 0
        while cur:       # 尾节点指向None，当未到达尾部时
            count += 1
            cur = cur.next
        return count

    # 查找节点是否存在
    def link_list_search(self, value_search):
        cur = self.head
        while cur:
            if cur.val == value_search:
                return True
            cur = cur.next
        return False

    # 遍历链表
    def travel_link_list(self):
        if not self.head:
            return None
        cur = self.head
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")

        # 使用生成器
        # if not self.head:
        #     return None
        # cur = self.head
        # yield cur.val
        # while cur.next:
        #     cur = cur.next
        #     yield cur.val




    # 根据索引返回链表节点
    def get_by_index(self, index:int):
        index = 0 if not isinstance(index, int) else index
        if index < 0 or index >= self.length:
            return -1
        else:
            cur = self.head
            count_index = 0
            while cur:
                if count_index == index:
                    return cur.val
                else:
                    count_index += 1
                    cur = cur.next

    # 头部添加元素
    def add_at_head(self, val):
        # 先创建一个保存val值的节点
        node = single_node(val)
        node.next = self.head      # node.next指向头结点
        self.head = node                # head指向node
        self.length += 1

    # 尾部添加元素
    def add_at_tail(self, val):
        node = single_node(val)
        if self.is_empty():             # 链表为空
            self.head = node
        # 非空，找到尾部
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.length += 1

    # 指定位置添加元素
    def add_at_index(self, index:int, val):
        index = 0 if not isinstance(index, int) else index
        if index <= 0:                      # 若指定的位置在第一个元素之前，则在头部插入
            self.add_at_head(val)
        elif index > (self.length - 1):     # 尾部插入
            self.add_at_tail(val)
        else:
            node = single_node(val)
            count_index = 0
            # pre用来指向指定位置pos的前一个位置pos-1
            pre = self.head
            while count_index < (index - 1):
                count_index += 1
                pre = pre.next
            node.next = pre.next            # 将新节点node指针next指向pre的next
            pre.next = node
            self.length += 1

    # 插入指定元素之后，找不到指定元素则插入尾部
    def add_after_value(self, value_insert, val):
        node = single_node(val)
        if self.is_empty():                 # 链表为空，直接插入
            self.head = node
            self.length += 1
        else:
            cur = self.head
            # cur.next为空或者cur.val等于指定元素，退出循环
            while cur.next and (cur.val != value_insert):
                cur = cur.next
            # 由于cur.next为None时，即尾节点也退出循环，无法判断尾节点，所以需再进行一次判断
            if cur.val == value_insert:
                node.next = cur.next
                cur.next = node
            else:
                cur.next = node         # 直接插入尾部
            self.length += 1

    # 删除指定位置元素
    def delete_by_index(self, index:int):
        # if self.is_empty():
        #     # return  -1
        #     raise IndexError("the link list is empty!")
        index = 0 if not isinstance(index, int) else index
        if index < 0 or index >= self.length or self.is_empty():
            raise IndexError("index is out of the range or the link list is empty!")
        elif index == 0:
            # 单独判断头节点
            self.head = self.head.next
            self.length -= 1
            return
        else:
            cur = self.head
            pre = None                  # 用来记录要删除的节点的前一个节点
            count_index = 0
            while count_index < index:
                pre = cur
                cur = cur.next
                count_index += 1
            pre.next = cur.next
            self.length -= 1

    # 删除指定元素
    def delete_by_value(self, value_delete):
        if self.is_empty():
            return "the link list is empty!"
        cur = self.head
        # 单独考虑头节点
        if cur.val == value_delete:
            self.head = self.head.next
            self.length -= 1
        else:
            pre = None                      # 用来记录要删除的节点的前一个节点
            while cur.next and cur.val != value_delete:
                pre = cur
                cur = cur.next
            # 由于cur.next为None时，即尾节点也退出循环，无法判断尾节点，所以需再进行一次判断
            if cur.val == value_delete:
                pre.next = cur.next
                self.length -= 1
            else:
                print("delete Fail ! can't find the value:{}".format(value_delete))

def main():
    link_list = my_link_list()

    link_list.add_at_head(11)
    link_list.add_at_tail(22)
    link_list.add_at_head(10)
    link_list.add_at_tail(33)
    link_list.add_at_tail(44)
    link_list.add_at_tail(55)
    link_list.add_at_tail(66)
    link_list.add_at_tail(77)
    link_list.add_at_index(0,'string')
    link_list.add_after_value(10010, 1011)
    link_list.travel_link_list()
    print(link_list.length)

    # 使用生成器的方法遍历
    # travel_list = list(link_list.travel_link_list())
    # for i in travel_list:
    #     print(i, end=" -> ")
    # print("None")

    link_list.delete_by_index(0)
    link_list.travel_link_list()
    link_list.delete_by_index(2)
    link_list.travel_link_list()
    link_list.delete_by_index(2)
    link_list.travel_link_list()
    print(link_list.length)

    link_list.delete_by_value(10)
    link_list.travel_link_list()
    print(link_list.length)

    print(link_list.link_list_search(10))



if __name__ == "__main__":
    main()