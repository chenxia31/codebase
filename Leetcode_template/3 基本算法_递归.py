#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024年9月26日 11:17:16
# @Author  : chenlongxu
# @Mail    : xuchenlong796@qq.com
#
# 描述 : 介绍递归的思想

''' 
递归 recursion 指的是通过重复将原问题分解成为同类子问题的解决方法，在绝大多数方法中采用 recall 自身的方式来实现递归

阶段 1：递归过程，将问题一层一层的转换成为和原问题形式、规模更小的子问题，在达到可以求解的程度和最小的问题规模之后进行求解，并返回子问题的求解
阶段 2：回归过程，通过底层问题的解开始逆向逐一回归，最终达到递推开始的问题，来返回原来问题的求解


为了使用递归的方式来求解问题，需要做的事情包块
1. 写出递推公式（核心找到原问题分解成为子问题的循环不变量）
2. 明确终止条件，如果没有终止条件会让递归无法结束，导致资源被诬陷占用
3. 将递推公式和终止条件翻译成为代码

def recursion(level, param1, param2, ...):
    if level > MAX_LEVEL:
        process_result
        return
    process(level, data, ...)
    recursion(level+1, p1, ...)
    # reverse the current level status if needed
'''


# 对数组进行归并排序
arr = [123,3543,65,634,235,4234]

def merge_sort(arr):
    ''' 
    回溯算法 核心在于寻找到循环不变量，将大的问题拆分成为小的问题

    以及确定最小的问题是什么
    '''
    if len(arr) <= 1:
        return arr
    
    middle = len(arr)//2
    left_merge = merge_sort(arr[:middle])
    right_merge = merge_sort(arr[middle:])

    res = []
    while left_merge and right_merge:
        if left_merge[0] > right_merge[0]:
            res.append(left_merge.pop(0))
        else:
            res.append(right_merge.pop(0))
    while left_merge:
        res.append(left_merge.pop(0))
    while right_merge:
        res.append(right_merge.pop(0))
    return res

arr = merge_sort(arr)
print(arr)


# 利用递归的思路来找到最深的二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    '''
    递归的思路来找到最深的二叉树
    '''
    if not root:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left, right) + 1
