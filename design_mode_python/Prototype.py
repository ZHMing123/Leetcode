# _*_ coding:utf-8 _*_
#文件作者: ZHMing123
#开发时间：2019/11/14 22:01
#文件名称：Prototype.py
#开发工具：PyCharm

"""
    Prototype(原型)
    原文链接：https://www.cnblogs.com/Liqiongyu/p/5916710.html
"""

import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update inner attributes dictionary"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


def main():
    class A:
        def __str__(self):
            return "I am A"

    a = A()
    prototype = Prototype()
    prototype.register_object('a', a)
    b = prototype.clone('a', a=1, b=2, c=3)

    print(a)
    print(b.a, b.b, b.c)



if __name__ == '__main__':
    main()
