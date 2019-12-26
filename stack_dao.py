# _*_ coding:utf-8 _*_
#文件作者: 郑海明
# 开发时间：2019/10/16 20:27
# 文件名称：stack_dao.py
# 开发工具：PyCharm


import random

"""
栈的顺序表的实现及一个应用：检验括号匹配问题：
"""


class my_stack():
    def __init__(self):
        self._elems = []

    # 判断栈是否为空
    def is_empty(self):
        return self._elems == []    # 注意：不能用None，此时不为空

    # 取出栈顶的元素，不删除
    def top(self):
        return self._elems[-1]

    # 入栈
    def push(self, val):
        self._elems.append(val)

    # 出栈
    def stack_pop(self):
        self._elems.pop()


"""
规则：
    1、左括号 -> push()入栈
    2、右括号 -> 查找栈顶（peek）是否是其匹配的右左括号，
                若匹配，出栈pop()，不匹配则返回False
    3、字符串结束 -> 栈为空，返回True, 不为空返回False
"""
# 判断字符串中的扩号是否匹配


def is_match(string: str):
    stack = []          # 基于list实现栈的push()和pop()(对应list.append()和list.pop())
    # 以右括号为健，方便下面分辨右括号
    paren_map = {')': '(', ']': '[', '}': '{'}
    for c in string:
        if c not in paren_map:      # 不是右括号（即为左括号）
            stack.append(c)         # 入栈
        # 如果栈为空，说明c没有匹配 or 栈顶的元素与c没有匹配
        elif not stack or paren_map[c] != stack.pop():
            return False
    return not stack                # 栈为空，返回True, 不为空返回False


def main():
    stack = my_stack()
    print(stack)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack._elems)
    print(stack.top())
    print(stack.stack_pop())
    print(stack._elems)

    string = "({{()}}{}[][])"
    print(is_match(string))


if __name__ == "__main__":
    main()
