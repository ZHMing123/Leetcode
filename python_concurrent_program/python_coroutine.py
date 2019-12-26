# _*_ coding:utf-8 _*_
#文件作者: ZHMing123
#开发时间：2019/11/26 21:52
#文件名称：python_coroutine.py
#开发工具：PyCharm

import asyncio
import time


"""
python 协程（Coroutine）
"""

# 在Python早期的版本中协程也是通过生成器来实现的，也就是基于生成器的协程（Generator-based Coroutines）
# 生产者-消费者模型
def producer(c):
    n = 0
    while n < 5:
        n += 1
        print('producer {}'.format(n))
        r = c.send(n)                   # send()：执行两步：先赋值，然后执行next()
        print('consumer return {}'.format(r))



def consumer():
    r = ''                  # 初始值r=None
    while True:
        n = yield r         # 执行到yield, 返回一个值r,下次执行send()时，赋值给n,执行到下一次遇到yield
        if not n:
            return          # n为0，退出函数consumer()
        print('consumer {}'.format(n))
        r = 'ok'


# 在Python3.5+版本新增了aysnc和await关键字
# 在函数定义时用async声明就定义了一个协程
'''
async def simple_async():
    """
    定义一个简单的协程
    注意：async对生成器是无效的。async无法将一个生成器转换成协程。
    :return:
    """
    print('hello')
    await asyncio.sleep(1)      # 休眠1秒
    print('python')

# 使用asyncio中的run方法运行一个协程
asyncio.run(simple_async())
'''

# asyncio.run()将运行传入的协程，负责管理asyncio事件循环。
# 除了run()方法可直接执行协程外，还可以使用事件循环loop
async def do_something(index):
    """
    # 在协程中如果要调用另一个协程就使用await。
    # 要注意await关键字要在async定义的函数中使用，而反过来async函数可以不出现await
    :param index:
    :return:
    """
    print(f'start {time.strftime("%X")}', index)

    """
    一旦协程阻塞,就会中断当前的协程处理,然后切换到下一个消息处理,
    同时把阻塞的协程加入消息队列的后面.
    """

    # 当使用异步模式的时候（每次调用await asyncio.sleep(1)），
    # 进程控制权会返回到主程序的消息循环里，并开始运行队列的其他任务（任务Ａ或者任务Ｂ）。
    await asyncio.sleep(1)      # asyncio.sleep()也是一个coroutine
    print(f'finished at {time.strftime("%X")}', index)


def test_do_something():
    # 生成器产生多个协程
    task = [do_something(i) for i in range(5)]

    # 获取一个事件循环
    loop = asyncio.get_event_loop()

    """
    第一步首先得到一个事件循环的应用也就是定义的对象loop。可以使用默认的事件循环，
    也可以实例化一个特定的循环类(比如uvloop),这里使用了默认循环run_until_complete(coro)
    方法用这个协程启动循环，协程返回时这个方法将停止循环。
    run_until_complete的参数是一个futrue对象。
    当传入一个协程，其内部会自动封装成task，其中task是Future的子类。
    """

    # 在事件循环中执行task列表
    loop.run_until_complete(asyncio.wait(task))
    loop.close()






if __name__ == "__main__":
    # c = consumer()
    # 如果生成器未启动，则必须在使用send()前必须要启动生成器，而启动的方法可以
    # 是generator.next()或是generator.send（None）执行到第一个yield处
    # next(c)                 # next(c)相当于send(None), 执行到yield,函数返回一次值，并暂停执行
    # producer(c)

    # test_do_something()
    """
    可以看出几乎同时启动了所有的协程。
    其实翻阅源码可知asyncio.run()的实现也是封装了loop对象及其调用。
    而asyncio.run()每次都会创建一个新的事件循环对象用于执行协程。
    """

    a = 257
    b = 257
    print(id(a))
    print(id(b))
    for i in range(-6, 1):
        print(id(i))
