# _*_ coding:utf-8 _*_
#文件作者: ZHMing123
#开发时间：2019/11/16 11:06
#文件名称：sort_algorithm.py
#开发工具：PyCharm

import time

def bubbleSort(arr):
    """
    冒泡排序：o(n^2)     稳定
    最好情况o(n)
    最坏情况o(n^2)
    空间复杂度o(1)
    :param arr:
    :return:
    """
    data_length = len(arr)
    if data_length <= 1:
        return arr
    for i in range(1, data_length):            # n - 1 轮
        has_translate = 0                      # 没有交换
        for j in range(0, data_length - i):    # 每轮 n - i 次（i：已经排好序的元素个数 - 1）
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                has_translate = 1
        if not has_translate:
            break
    return arr


def select_sort(arr):
    """
    选择排序：o(n^2)     不稳定
    最好情况o(n^2)
    最坏情况o(n^2)
    空间复杂度o(1)
    :param arr:
    :return:
    """
    data_length = len(arr)
    if data_length <= 1:
        return arr
    for i in range(0, data_length - 1):            # i: 未排序序列的第一个元素
        min_index = i                           # 记录最小元素的索引
        for j in range(i + 1, data_length):
            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index:                      # i所在位置不是最小元素
            arr[i], arr[min_index] = arr[min_index], arr[i]     # 交换
    return arr


def insert_sort(arr):
    """
    插入排序：o(n^2)     稳定
    最好情况o(n)
    最坏情况o(n^2)
    空间复杂度o(1)
    :param arr:
    :return:
    """
    data_length = len(arr)
    if data_length <= 1:
        return arr
    for i in range(1, data_length):                 # n - 1 轮， 第一个元素已排好序
        preIndex = i -1
        current = arr[i]                            # 记录当前要排序的元素
        # 向前找，比current大， 后移一位，直至找到比current小或等于current的，插入其后面
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current               # 找到比current小或等于current的，插入其后面
    return arr


def shell_sort(arr):
    """
    希尔排序（插入排序的更高效版本）：o(n log n)  准确：o(1.3n)     不稳定
    最好情况 o(n log n)
    最坏情况o(n^2)
    空间复杂度o(1)
    :param arr:
    :return:
    """
    data_length = len(arr)
    if data_length <= 1:
        return arr
    gap = data_length // 2                          # 初始步长
    while gap > 0:                                  # gap = 0 时退出循环
        for i in range(gap, data_length):           # 插入排序
            pre_Index = i - gap
            current = arr[i]
            # 向前找，比current大， 后移一位，直至找到比current小或等于current的，插入其后面
            while pre_Index >= 0 and arr[pre_Index] > current:
                arr[pre_Index+gap] = arr[pre_Index]
                pre_Index -= gap
            arr[pre_Index+gap] = current        # 找到比current小或等于current的，插入其后面
        gap = gap // 2                          # 整除
    return arr


def merge_sort(arr):
    """
    拆分序列
    归并排序：o(n log n)     稳定
    最好情况o(n log n)
    最坏情况o(n log n)
    空间复杂度o(n)
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left, right = arr[0:middle], arr[middle: ]
    return  merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    """
    合并两个有序序列为一个
    :return:
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 将剩余的元素拷贝到result中
    result += left[i: ]
    result += right[j: ]

    # # 方法二：
    # while left and right:           # 两者非空
    #     if left[0] <= right[0]:
    #         result.append(left.pop(0))
    #     else:
    #         result.append(right.pop(0))
    # while left:                     # 将剩余的元素拷贝到result中
    #     result.append(left.pop(0))
    # while right:
    #     result.append(right.pop(0))

    return result


def quick_sort(arr, left=None, right=None):
    """
    快速排序：o(n log n)     不稳定
    最好情况o(n log n)
    最坏情况o(n^2)   但这种情况不常见
    空间复杂度o(log n)  递归过程需要记住每次的基准值
    :param arr:
    :return:
    """
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr)-1 if not isinstance(right, (int, float)) else right
    if left < right:            # 还可以拆分
        partitionIndex = partition(arr, left, right)
        # 边界值位于已经位于正确位置了，不用参与下次排序了
        quick_sort(arr, left, partitionIndex - 1)
        quick_sort(arr, partitionIndex + 1, right)

    return arr


def partition(arr, left, right):
    """
    返回经过-轮排序后基准在数组中的位置
    :param arr:
    :param left:
    :param right:
    :return:
    """
    pivot = left            # 基准pivot(以第一个元素为基准)
    index = pivot + 1       # 慢指针，用于记录最前面那个比基准大的元素的位置
    i = index               # 快指针，用于遍历
    while i <= right:       # 还没有遍历完整个数组
        if arr[i] < arr[pivot] :
            arr[i], arr[index] = arr[index], arr[i]         # 交换
            index += 1
        i += 1              # 遍历下一个元素

    arr[pivot], arr[index-1] = arr[index-1], arr[pivot]     # 将基准放回中间位置（不一定是绝对的中间）

    return index - 1        # index是最前面那个比基准大的元素的位置，所以返回index - 1


def quickSort(arr, left=None, right=None):
    """
    快速排序的另一种实现：前后两个指针分别从两头向中间移动
    :param arr:
    :param left:
    :param right:
    :return:
    """
    # 这个只有第一次进来的时候作用， 后面的调用传参时确保了left, right的正确的
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr)-1 if not isinstance(right, (int, float)) else right

    pivot = arr[left]           # 基准
    lower_index = left + 1      # 左指针，从左到右遍历(除去基准元素）
    upper_index = right         # 右指针
    while lower_index <= upper_index:           # 没有交叉
        while arr[lower_index] < pivot:         # 找到比基准大或者等于基准的元素
            lower_index += 1
        while arr[upper_index] > pivot:         # 找到比基准小或者等于基准的元素
            upper_index -= 1

        if lower_index < upper_index:
            arr[lower_index], arr[upper_index] = arr[upper_index], arr[lower_index] # 交换
            lower_index += 1
            upper_index -= 1
        else:                   # lower_index == upper_index时，lower_idex + 1退出循环
            lower_index += 1

    # 将基准放回中间位置，upper_index最终指向的元素一定是小于或等于基准的，所以应该跟upper_index换
    arr[left], arr[upper_index] = arr[upper_index], arr[left]

    if left < upper_index - 1:  # 前半部分数组还可以再划分
        quickSort(arr, left, upper_index - 1)
    if upper_index + 1 < right: # 后半部分数组还可以再划分
        quickSort(arr, upper_index + 1, right)

    return arr


def build_max_heap(arr):
    """
    # 将初始的列表构建大顶堆
    :param arr:
    :return:
    """
    for i in range(len(arr) // 2 - 1, -1, -1):          # 从最后一个非叶子节点len(arr)//2 - 1倒序取到0
        heapify(arr, i)


def heapify(arr, i):
    """
    调整节点，使其满足大顶堆结构（子节点小于或等于其父节点）
    :param arr:
    :param i:
    :return:
    """
    left = 2*i + 1          # 左子节点在数组中的位置
    right = 2*i + 2
    largest = i             # i表示当前需要调整的节点
    if left < arr_len and arr[left] > arr[largest]:    # 左子节点比其父节点大
        largest = left
    if right < arr_len and arr[right] > arr[largest]:  # 右子节点比其父节点大
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]     # 与最大的那个子节点交换值
        heapify(arr, largest)                           # 对交换的子节点的子树递归调用，继续调整


def heap_sort(arr):
    """
    堆排序o(n log n)   不稳定
    最好情况o(n log n)
    最坏情况o(n log n)
    空间复杂度o(1)
    :param arr:
    :return:
    """
    global arr_len
    arr_len = len(arr)          # 定义一个全局变量，因为堆顶和堆尾交换后，堆尾就排好了序
    if arr_len < 2:
        return arr

    build_max_heap(arr)         # 将初始的列表构建为大顶堆
    for i in range(len(arr)-1, 0, -1):      # 从最后一个元素：len（arr)-1 向前取
        arr[0], arr[i] = arr[i], arr[0]     # 交换堆顶和堆尾元素
        arr_len -= 1                        # 待排序的数组长度减 1
        heapify(arr, 0)                     # 以后的每次调整只需对根节点进行调整便可以

    return arr


def count_sort(arr):
    """
    计数排序（稳定版本） o(n + k)
    最好情况o(n + k)
    最坏情况o(n + k)
    空间复杂度o(n)
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    # 1、得到序列的最大最小值，并计算出插值d
    arr_max = arr[0]
    arr_min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > arr_max:
            arr_max = arr[i]
        if arr[i] < arr_min:
            arr_min = arr[i]
    count_array = [0] * (arr_max - arr_min + 1)       # 创建并初始化计数数组值均为0

    # 2、遍历原数组，计数
    for i in range(0, len(arr)):
        count_array[arr[i]- arr_min] += 1

    # 3、统计数组变形，后面元素等于前面元素之和
    for i in range(1, len(count_array)):
        count_array[i] = count_array[i] + count_array[i-1]

    # 4、倒序遍历原始序列，从统计数组中找到正确位置， 输出结果
    sorted_result = [0] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        sorted_result[count_array[arr[i] - arr_min] - 1] = arr[i]   # -1 是因为sorted_result是从0开始的，所以是位置-1
        count_array[arr[i] - arr_min] -= 1                          # 计数 -1

    return sorted_result


def bucket_sort(arr, bucketsize):
    """
    桶排序 o(n + k + n log n/k)
    最好情况o(n + k)
    最坏情况o(n^2)
    空间复杂度o(n + k)
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    # 1、得到序列的最大最小值，并计算出插值d
    arr_max = arr[0]
    arr_min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > arr_max:
            arr_max = arr[i]
        if arr[i] < arr_min:
            arr_min = arr[i]
    arr_range = arr_max - arr_min       # 数组的差值， +1 后：表示数组的范围

    # 2、桶的数量（可动态设置，bucketsize:假设均匀分布，期望每个桶有多少数据）
    bucket_num = (arr_range + 1) // bucketsize
    # 对应的桶
    bucket_lists = list([] for _ in range(bucket_num))     # 相当于一个二维数组[ [], [], ...]

    # 3、遍历原数组，将数据放入对应的桶中
    for data in arr:
        bucket_index = (data - arr_min) * (bucket_num - 1) // arr_range     # 因为下标是从0开始的，所以要bucket_num - 1
        bucket_lists[bucket_index].append(data)                 # 放入对应的桶中

    #4、桶内排序（可以使用快速排序：不稳定， 或者插入排序：稳定）
    for bucket in bucket_lists:
        # quick_sort(bucket)
        insert_sort(bucket)

    # 5、合并输出结果
    sorted_result = []
    for bucket in bucket_lists:
        if len(bucket) != 0:        # 桶不为空
            sorted_result.extend(bucket)        # bucket本身就是list形式，用extend
    return sorted_result


def radix_sort(arr, k):
    """
    基数排序（桶排序的一种扩展） o(n * k)
    最好情况o(n * k)
    最坏情况o(n * k)
    空间复杂度o(n + k)
    :param arr:
    :param k: 元素的最大长度（迭代轮数）
    :return:
    """
    if len(arr) < 2:
        return arr
    a = 0
    while a < k:
        bucket_lists = list([] for _ in range(10))          # 0-9号桶
        # 1、遍历数组，分桶（按当前从右往左数的第a个元素来分）
        for data in arr:
            bucket_index = (data // 10**a) % 10           # 当前位置的数值取余10得桶的序号
            bucket_lists[bucket_index].append(data)

        # clear()函数用于清空列表，类似于del a[:]
        arr.clear()        # 用来保存每一轮迭代的中间结果，供下一轮迭代使用
        # 依次从每个桶中取出元素，放到arr中
        for bucket in bucket_lists:
            for data in bucket:
                arr.append(data)
        a += 1

    return arr


def radix_sort_string(arr, max_length):
    """
    # 字符串排序:按字母顺序输出（基于基数排序，假设字符串均由小写的英文字母组成（97-122））
    # chr(x): 返回Unicode编码x对应的字符
    # ord(x): 返回单字符x对应的Unicode编码
    # 采用LSD(低位优先进行排序)，长度不足k的低位补0，排序时把0当成比a更小的字符
    :param arr:
    :param max_length: 最长的字符串的长度（迭代次数）
    :return:
    """
    if len(arr) < 2:
        return arr

    for k in range(max_length, 0, -1):                        # 从左往右第k位字符(下标从1开始数)
        bucket_lists = list([] for _ in range(27))      # 0-26号桶：表示0，字母a-z

        # 1、遍历数组，分桶（按当前从左往右数的第k个元素来分）
        # 获取字符串第k位字符的桶序号，字符串长度小于k的分到0号桶
        global bucket_index
        for data in arr:
            if len(data) < k:
                bucket_index = 0                        # 字符串长度小于k的分到0号桶
                bucket_lists[bucket_index].append(data)
            else:
                # ord(x): 返回单字符x对应的Unicode编码
                a = 1
                for i in data:                              # 获取字符串的第k个字符
                    if a == k:
                        # print(ord(i) - ord('a') + 1)        # +1 是因为a是1号桶而不是0号桶
                        bucket_index = ord(i) - ord('a') + 1
                        bucket_lists[bucket_index].append(data)
                        break
                    a += 1



        # clear()函数用于清空列表，类似于del a[:]
        arr.clear()  # 用来保存每一轮迭代的中间结果，供下一轮迭代使用
        # 依次从每个桶中取出元素，放到arr中
        for bucket in bucket_lists:
            if len(bucket) != 0:
                arr.extend(bucket)
        # for bucket in bucket_lists:
        #     for data in bucket:
        #         arr.append(data)
        # print(arr)

    return arr





if __name__ == "__main__":
    input_data = []
    with open('data.txt', 'r') as f:
        for line in f.readlines():
            data_line = line.strip().split("\t")
            for data in data_line:
                input_data.append(int(data))
    print(input_data)

    start = time.time()
    # bubbleSort(input_data)
    # select_sort(input_data)
    # select_sort(input_data)
    # select_sort(input_data)
    # result = merge_sort(input_data)
    # print(result)
    # print(quick_sort(input_data))
    # print(quickSort(input_data))
    # print(heap_sort(input_data))
    # print(count_sort(input_data))
    # print(bucket_sort(input_data,10))
    # print(radix_sort(input_data, 5))
    end = time.time()
    # print(input_data)
    print("cost time:{}".format(end - start))

    # 字符串排序
    string_list = ['qd', 'abc', 'qwe', 'hhb', 'a', 'cws', 'ope']
    print(radix_sort_string(string_list, 3))

    string_data = "In China students have to learn English since they went to school Some parents even hire a tutor to " \
                  "let theirchildren master English when they are very small In western countries a lot of people learn " \
                  "mandarin just as we learn English They want to master Chinese because China is the future market Look " \
                  "back on the past decades Chinese economy developed so fast that the foreign media were shocked They " \
                  "predicted that Chinese economy would be in the coming year To learn Chinese well is to seize the " \
                  "chance so more and more foreign parents send their children to learn Chinese Some even can speak " \
                  "as well as a local people"

    # print(string_data.lower())
    string_word = []
    for word in string_data.lower().split(' '):
        string_word.append(word)
    print(string_word)
    print(radix_sort_string(string_word, 13))





















