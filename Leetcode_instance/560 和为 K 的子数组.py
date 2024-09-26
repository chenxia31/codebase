#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024年9月26日 11:13:15
# @Author  : chenlongxu
# @Mail    : xuchenlong796@qq.com
#
# 描述: 力扣 560 和为 K 的子数组

# 题目描述：给定一个整数数组num 和整数 l，统计数组中 k 的连续子数组的数量
# 这里可以采用前缀和的方式来进行计算

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
def subarraySum(nums, k):
    '''
    前缀和的方式来进行计算
    '''
    hashmap = {0:1}
    pre_sum = 0
    count = 0
    for num in nums:
        pre_sum += num
        if pre_sum - k in hashmap:
            count += hashmap[pre_sum - k]
        hashmap[pre_sum] = hashmap.get(pre_sum, 0) + 1
    return count

nums = [1,1,1]
k = 2
subarraySum(nums, k)