#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024年9月26日 10:24:05
# @Author  : chenlongxu
# @Mail    : xuchenlong796@qq.com
#
# 对常见的排序算法进行总结，包括 冒泡排序、选择排序、插入排序、归并排序、快速排序


import random

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

def bubble_sort(arr):
    '''
    冒泡排序 Bubble sort 是通过相邻元素的比较来将最小元素从后面移动到前面,这个写法是选择排序吧
    '''
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            # 每一轮循环来-i实现最大值的冒泡
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


def selection_sort(arr):
    '''
    选择排序: 每次选择一个最小的元素放在前面
    '''
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            # 每一轮循环将
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr

def quick_sort(arr):
    '''
    快速排序 quick sort 是从 arr 中随机选择一个基准值，再根据这个基准值来进行排序
    '''
    if len(arr) <= 1:
        return arr
    baseline = random.choice(arr)
    left = [x for x in arr if x<baseline]
    right = [x for x in arr if x > baseline]
    return quick_sort(left) + [baseline] + quick_sort(right)

def classic_quick_sort(arr,low,high):
    '''
    快速排序经典方法，选择 baseline 之后，如何在不使用额外空间复杂度的情况下完成元素的互换,因此在每次传参的过程中
    并不直接传递 arr 而是选择待排序的下标 来避免复杂的空间复杂度，在这样的情况下，上述生成子数组的方式由生成一个新数组，需要
    转换成为一种原地的方式

    由此经典：
    1. 函数本身只完成对于 arr 传入的 low high之间的排序 因此初始值为 0-n-1
    2. 每次随机的选择一个 baseline，通过替换的方式来将小于 baseline 的替换到 left，将大于baseline 的方式替换到右边
    3. 每次返回baseline 在数组中的位置下标，并将左边和右边的数组继续送入进行排序
    4. 每次循环的遍历结束条件就是是否为单个元素
    '''
    if low >= high:
        ''' 
        说明遍历可以结束了
        '''
        return 
    # 通过一次遍历将 arr 中比 baseline 小的值迁移到左边，将 baseline 大的值迁移到右边
    baseline = arr[low] # 随机选择一个元素
    # 注意这里我们只需要做一次排序就好了，所以每次选择左边大于 arr 的，和右边小于 baseline 的之间进行互换即可，并不需要有顺序瓜子
    left = low 
    right = high 
    while left < right:
        # 从右侧开始找到一个最小的数
        # 仔细思考为什么这里可以实现原地的迁移
        while left < right and arr[right] >= baseline:
            right -= 1
        while left < right and arr[left] <= baseline:
            left += 1
        if left < right:
            arr[left],arr[right] = arr[right],arr[left]
    arr[low],arr[left] = arr[left],arr[low]
    print(arr)
    classic_quick_sort(arr,low,left-1)
    classic_quick_sort(arr,left+1,high)

arr = [random.randint(0, 100) for _ in range(10)]
classic_quick_sort(arr,0,len(arr)-1)
print('class quick sort result is {arr}'.format(arr = arr))
        
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


# def quick_sort(arr, low, high):
#     '''
#     快速排序的步骤包括：
#     1. 随机选择一个 pivot（基准值）作为参考，左侧小于 pivot，右侧大于 pivot。
#     2. 使用指针 left 和 right，分别找到不符合条件的元素进行交换。
#     3. 当 left 和 right 指针相遇时，将 pivot 放到正确的位置。
#     4. 递归地对 pivot 左右两边的数组继续执行上述过程。
#     '''
#     if low < high:  # 添加递归的边界条件
#         pivot = arr[low]  # 选择第一个元素作为基准
#         left = low
#         right = high

#         while left < right:
#             # 从右侧开始找比 pivot 小的数
#             while left < right and arr[right] >= pivot:
#                 right -= 1
#             # 从左侧开始找比 pivot 大的数
#             while left < right and arr[left] <= pivot:
#                 left += 1
#             if left < right:
#                 # 确定边界
#                 arr[left], arr[right] = arr[right], arr[left]  # 交换元素

#         arr[low], arr[left] = arr[left], arr[low]  # 将 pivot 放到正确位置
#         # 递归处理左右两部分
#         quick_sort(arr, low, left - 1)
#         quick_sort(arr, left + 1, high)


# # 快速排序的本质是将归并排序的结果汇合放在前面
# def quick_sort(arr,low,high):
#     if low < high:
#         # 只有归并的时候才能继续
#         left = low 
#         right = high 
#         pivot = arr[low]
#         while left < right:
#             while left < right and arr[right] >= pivot:
#                 right -= 1
#             while left < right and arr[left] <= pivot:
#                 left += 1
#             if left < right:
#                 arr[left],arr[right] = arr[right],arr[left]
#         arr[left],arr[low] = arr[low],arr[right]
#         quick_sort(arr,low,left-1)
#         quick_sort(arr,left+1,high)

if __name__ == '__main__':
    # 选择而不同的排序算法
    sort_func = {
        'bubble_sort': bubble_sort,
        'selection_sort': selection_sort,
        # 'merge_sort': merge_sort,
        'quick_sort': quick_sort
    }
    # for key in sort_func:
    #     arr = [random.randint(0, 100) for _ in range(100)]
    #     print('Input arr is {arr}'.format(arr=arr))
    #     print(f'Function {key} output: {sort_func[key](arr)}')
