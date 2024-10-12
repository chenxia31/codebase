#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : Oct 11, 2024 at 14:41:46
# @Author  : chenlongxu
# @Mail    : xuchenlong796@qq.com
#
# 描述 介绍数组数据结构中常见的技巧，包括：双指针、滑动窗口、二分查找、前缀和、差分、位运算
import random 
'''
双指针技巧
'''
# 1. 两数之和, 借助并查集的方式来寻找两个数的有序对

def two_sum(arr,target):
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] + arr[right] == target:
            return [arr[left],arr[right]]
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return []

arr = [random.randint(0,100) for _ in range(10)]
arr.sort()


'''
二分查找

关键在于确定自己的目标函数，并不断的缩小自己的可行范围来进行查找]
二分查找的算法流程可以分为：
1. 首先确定可行域，边界的起点和重点
2. 选择一个边界中的较小值来进行查找
3. 判断边界值对应的输出值是否满足 target 条件
4. 如果满足条件则返回，如果不满足条件则进行下一轮查找

对应的问题包括：
1. 如何确定区间的开闭问题
2. 如何寻找到合适的 mid
3. 边界条件的判断，是否包含等于
4. 搜索区间范围的选择
'''

def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

'''
寻找旋转数组的最小值
'''
def find_min(arr):
    left = 0
    right = len(arr)-1
    baseline = arr[0]
    while left < right:
        mid = (left+right)//2
        if arr[mid] > baseline:
            left = mid + 1
        else:
            right = mid
    return arr[left]

arr = [3,4,5,1,2]
print(find_min(arr))


''' 
接雨水问题
'''
height = [0,1,0,2,1,0,1,3,2,1,2,1]

def trap(arr):
    '''
    给定 n 个非负整数的宽度为 1 的高度柱子
    计算按照这个排列的柱子在下雨之后可以接多少的雨水

    求解算法：
    1. 遍历方法 enumerate：利用动态规划和前缀和的方式来计算每个点左边的最大值和右边的最大值，计算的方式为 min(max_left,max_right) - nums[i] 也就是最终的的结果
    2. 单调栈的方法，通过对单调栈维护过程中的进栈和出栈的过程进行记录，来实现最终值的计算
    3. 双指针的方法
    '''
    if not height:
        return 0 
    n = len(height)

    left_max = [0 for _ in range(n)]
    left_max[0] = height[0]
    right_max = [0 for _ in range(n)]
    right_max[-1] = height[-1]

    for i in range(1,n):
        left_max[i] = max(left_max[i-1],height[i])
    
    for i in range(n-2,-1,-1):
        right_max[i] = max(right_max[i+1],height[i])
    
    res = 0
    for i in range(n):
        temp = min(left_max[i],right_max[i]) - height[i]
        if temp > 0:
            res += temp
    return res

print(trap(height))