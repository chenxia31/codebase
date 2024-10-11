#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : Oct 11, 2024 at 11:28:51
# @Author  : chenlongxu
# @Mail    : xuchenlong796@qq.com
#
# 描述： 为暑期 IEG 提出来的算法题，这里使用再重新复习一下


'''
题目描述, 给定一个包含红色，白色和蓝色球的数组，要求原地进行分类，要求按照白色、红色和蓝色顺序进行排列
红色 0
白色 1
蓝色 2 

输出的顺序为 111,000,222
'''
input = [1,2,0,1,2,0]
output = [1,1,0,0,2,2]

# 第一步将所有的 2 替换到最右边
# 第二步将所有的 1 替换到最左边

def solution(input):
    left = 0
    right = len(input)-1
    while left < right:
        while left < right and input[right] == 2:
            # 找到第一个不是 2 的数
            right -= 1
        while left < right and input[left] != 2:
            # 找到第一个是 2 的数
            left += 1
        input[left],input[right] = input[right],input[left]
    low = 0
    high = right
    print('Next step is from {begin} to {end} with {arr}'.format(begin=low,end=high,arr = input))
    while low < high:
        while low < high and input[high] == 0:
            # 找到第一个不是 0 的数
            high -= 1
        while low < high and input[low] != 0:
            # 找到第一个是 0 的数
            low += 1
        input[low],input[high] = input[high],input[low]
    return input

solution(input)
print(input)


'''
Top K 问题
利用快速排序完成，但是只完成最后的 k 个数，并不需要完成全部的排序

针对前者如果小于那个元素完成 K，后面的并不需要完成排序
'''
def top_k(arr,k):
    def quick_sort(arr,low,high):
        # 重点在于递归的时候也要将判断加进去
        if low == k and high == k:
            return arr[:k]
        if low < high:
            baseline = arr[low]
            left = low
            right = high
            while left < right:
                while left < right and arr[right] >= baseline:
                    right -= 1
                while left < right and arr[left] <= baseline:
                    left += 1
                if left < right:
                    arr[left],arr[right] = arr[right],arr[left]
            arr[low],arr[left] = arr[left],arr[low] # 每次选择完都是 left + baseline + right
            if left == k:
                return arr[:k] # 返回较小的 k 个数
            elif left > k:
                return quick_sort(arr,low,left-1)  # 递归处理左侧
            else:
                return quick_sort(arr,left+1,high)
    return quick_sort(arr,0,len(arr)-1)

arr = [3,2,1,5,6,4]
k = 5
print(top_k(arr,k))