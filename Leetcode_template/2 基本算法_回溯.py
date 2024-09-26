#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024年9月26日 10:26:50
# @Author  : chenlongxu
# @Mail    : xuchenlong796@qq.com
#
# 描述 ：
res = []
path = []
# def backtracking_template(nums):
#     '''
#     回溯算法：采用一种避免不必要搜索的枚举搜索算法的框架，采用试错的方式来寻找问题的求解。当探索到某一步中发现原先的选择不满足求解条件之后，退回展开回溯进行重新选择

#     如何确定使用回溯算法：
#     1. 根据所给的问题，定义问题的解空间。确定解空间的大小
#     2. 确定解空间的组织方法
#     3. 利用深度优先的策略对解空间进行搜索，
#     '''
#     if is_terminate():
#         res.append(path)
    
#     for i in range(nums):
#         if is_continue():
#             path.append()


# 问题 1 给定不含重复数字的数组 nums，返回所有可能的全排列的组会
nums = [1,2,3,4]
# 1 第一种方法是使用二进制的方式来生成所有可能的排列方案，进而得到最终的全排列的组会
# 2 第二种方法是采用回溯的方法来求解出最终的结果，核心采用递归的方式来找到对应的排列组合
res = []
path = []
def backtracking(nums):
    # terminal state
    if len(path) == len(nums):
        res.append(path[:])
        return 
    for i in range(len(nums)):
        if nums[i] not in path:
            path.append(nums[i])
            backtracking(nums)
            path.pop() # 撤销对应的操作
backtracking(nums)
print(res)


# 问题 2 长度为 n 的数组 ，求出长度为 k 的子集
def subsets(nums):
    res = []
    path = []
    def backtracking(start):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtracking(i+1)
            path.pop()
    backtracking(0)
    return res