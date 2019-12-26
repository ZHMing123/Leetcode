# _*_ coding:utf-8 _*_
#文件作者: 郑海明
#开发时间：2019/10/15 8:34
#文件名称：141.Linked List Cycle.py
#开发工具：PyCharm


import sys
import random


"""
使用python建立简单的单链表
"""
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

# 将列表转换成链表
def list_to_link(list):
    dummy_root = ListNode(0)        # 根（Head节点）
    ptr = dummy_root                # 指向head
    for number in list:
        ptr.next = ListNode(number)
        ptr = ptr.next
    # 链表尾部
    tail = ptr
    print("tail.value:{}, tail.next:{}".format(tail.val, tail.next))
    ptr = dummy_root.next           # 指向第一个节点（相当于head）

    if len(list) < 2:
        return "Can not generate a link cyle!"
    # 生成有环链表
    index = random.randint(0, len(list) - 2)
    print('index:%d' % index)
    count = 0
    cur = ptr
    while count < index:
        print(cur.val)
        cur = cur.next
        count += 1
    tail.next = cur           # 将尾节点指针指向cur,形成环
    return ptr

# 遍历链表
def travel_link(head):
    # 无环链表的遍历
    res = head
    while res is not None:          # 非空
        print(res.val, end=' -> ')
        res = res.next
    print('None')


# 判断链表是否有环
# 方法一：快慢指针法
def has_cycle(head):
    fast = slow = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:            # fast和slow相遇，证明有环
            return True
    return False

# 方法二：set 判重 o(n)
def has_cycle_method2(head):
    hash_map = dict()
    cur = head
    while cur:
        print(cur)
        if cur in hash_map:
            return True
        hash_map[cur] = None
        cur = cur.next
    print(hash_map)
    return False

"""
# 如果链表有环，返回入环节点
# 当确定有环后，慢指针重新回到头节点，快指针停留在相遇处，
# 然后两个指针每次移动1个节点，最终他们在入环节点处相。
"""
def find_entry_of_cycle(head):
    fast = slow = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:            # fast和slow相遇，证明有环
            break
    if not fast or not fast.next:   # 跳出循环的条件为None，即无环
        return None
    slow = head                     # 当确定有环后，慢指针重新回到头节点
    while slow is not fast:         # 还没有相遇
        slow = slow.next
        fast = fast.next
    return (slow, slow.val)

def main():
    print("please input link's values:")
    line = sys.stdin.readline().strip()
    value_list = list(map(int, line.split()))
    # 建立链表
    head = list_to_link(value_list)
    print(head)
    # 遍历链表
    # travel_link(head)
    print(has_cycle(head))
    print(find_entry_of_cycle(head))

    print(has_cycle_method2(head))

if __name__ == "__main__":
    # test_numbers:99 88 77 44 11 22 33 66 55
    main()