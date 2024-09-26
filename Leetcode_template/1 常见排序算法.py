#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024年9月26日 10:24:05
# @Author  : chenlongxu
# @Mail    : xuchenlong796@qq.com
#
# 对常见的排序算法进行总结，包括 冒泡排序、选择排序、插入排序、归并排序、快速排序


arr = [1, 3, 2, 5, 4, 7, 6, 9, 8]
######################
# inputs: 无序数组
# outputs: 有序数组
######################
# 定义一个修饰器，用于计算函数运行时间，以及函数的输入输出
def timer(func):
    def wrapper(*args, **kwargs):
        # Q1: args 和 kwargs 是什么？
        # A1: *args 和 **kwargs 是 python 中的可变参数，*args 表示任意多个无名参数，类型为 tuple；**kwargs 表示关键字参数，类型为 dict
        import time
        print(f'Function {func.__name__} input: {args}')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('Func{} run time: {}'.format(func.__name__, round(end_time-start_time),2))
        print(f'Function {func.__name__} output: {result}')
        return result
    return wrapper

@timer
def bubble_sort(arr):
    ''' 
    冒泡排序
    '''
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
bubble_sort(arr)


@ timer
def selection_sort(arr):
    '''
    选择排序: 每次选择一个最小的元素放在前面
    '''
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
selection_sort(arr)

@timer
def merge_sort(arr):
    ''' 
    归并排序：利用分治法，实现元素的排序 
    1. 思考如何将一个大的问题转换成为一个可以分解的小的问题
    2. 思考如何解决这个最小的问题
    问题整体可以被一步一步的完成
    '''
    middle = len(arr)//2
    if len(arr) == 1 or len(arr) == 0:
        return arr 
    arr_left = merge_sort(arr[:middle])
    arr_right = merge_sort(arr[middle:])
    # 如何将两个问题分别完成
    res = []
    while arr_left and arr_right:
        if arr_left[0] < arr_right[0]:
            res.append(arr_left.pop(0))
        else:
            res.append(arr_right.pop(0))
    while arr_left:
        res.append(arr_left.pop(0))
    while arr_right:
        res.append(arr_right.pop(0))
    return res 
# merge_sort(arr)


def quick_sort(arr, low, high):
    '''
    快速排序的步骤包括：
    1. 随机选择一个 pivot（基准值）作为参考，左侧小于 pivot，右侧大于 pivot。
    2. 使用指针 left 和 right，分别找到不符合条件的元素进行交换。
    3. 当 left 和 right 指针相遇时，将 pivot 放到正确的位置。
    4. 递归地对 pivot 左右两边的数组继续执行上述过程。
    '''
    if low < high:  # 添加递归的边界条件
        pivot = arr[low]  # 选择第一个元素作为基准
        left = low
        right = high

        while left < right:
            # 从右侧开始找比 pivot 小的数
            while left < right and arr[right] >= pivot:
                right -= 1
            # 从左侧开始找比 pivot 大的数
            while left < right and arr[left] <= pivot:
                left += 1
            if left < right:
                # 确定边界
                arr[left], arr[right] = arr[right], arr[left]  # 交换元素

        arr[low], arr[left] = arr[left], arr[low]  # 将 pivot 放到正确位置
        # 递归处理左右两部分
        quick_sort(arr, low, left - 1)
        quick_sort(arr, left + 1, high)

# 示例用法
arr = [38, 27, 43, 3, 9, 82, 10]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

# 快速排序的本质是将归并排序的结果汇合放在前面
def quick_sort(arr,low,high):
    if low < high:
        # 只有归并的时候才能继续
        left = low 
        right = high 
        pivot = arr[low]
        while left < right:
            while left < right and arr[right] >= pivot:
                right -= 1
            while left < right and arr[left] <= pivot:
                left += 1
            if left < right:
                arr[left],arr[right] = arr[right],arr[left]
        arr[left],arr[low] = arr[low],arr[right]
        quick_sort(arr,low,left-1)
        quick_sort(arr,left+1,high)

quick_sort(arr,0,len(arr)-1)
print(arr)