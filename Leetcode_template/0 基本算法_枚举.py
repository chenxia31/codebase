#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024年9月26日 10:28:17
# @Author  : chenlongxu
# @Mail    : xuchenlong796@qq.com
#
# 描述 ：介绍枚举算法的常用思路

'''
枚举算法简介：根据问题的性质列出所有问题的所有可能解，在枚举的过程中，将其余 target 比较得到满足问题的解，在这个过程中
1. 要求准确的表达问题的状态空间
2. 要求能够遍历所有的状态空间，不能遗漏也不能重复
3. 在穷举的基础上来实现优化，包括剪枝的操作
'''

def timer(func):
    def wrapper(*args, **kwargs):
        # Q1: args 和 kwargs 是什么？
        # A1: *args 和 **kwargs 是 python 中的可变参数，*args 表示任意多个无名参数，类型为 tuple；**kwargs 表示关键字参数，类型为 dict
        import time
        # print(f'Function {func.__name__} input: {args}')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('Func{} run time: {}'.format(func.__name__, round(end_time-start_time),10))
        print(f'Function {func.__name__} output: {result}')
        return result
    return wrapper

# 问题1 ： 两数之和
@timer
def force_two_sum(nums, target):
    '''
    暴力求解
    '''
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

@timer
def two_sum(nums, target):
    '''
    在暴力求解的基础上加入状态空间的优化
    '''
    hashmap = {}
    for i in range(len(nums)):
        if target - nums[i] in hashmap:
            return [hashmap[target-nums[i]], i]
        hashmap[nums[i]] = i
    return []

# 生成一个 100000 的数组
arr = [i for i in range(100000)]
target = 9
# print(force_two_sum(arr, target))
# print(two_sum(arr, target))

# 问题 3 找到小于 N 的所有的prime number
@timer
def force_prime_number(n):
    '''
    找到小于 n 的所有的 prime number
    '''
    res = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            res.append(i)
    return res

# 利用素数筛选法来实现
@timer
def prime_number(n):
    '''
    利用素数筛选法来实现
    '''
    res = []
    is_prime = [1] * n
    for i in range(2, n):
        if is_prime[i]:
            res.append(i)
            for j in range(i*i, n, i):
                is_prime[j] = 0
    return res

print(force_prime_number(1000000))
print(prime_number(1000000))


# 问题 3 统计平方和的三元组的个数
# 返回满足 a^2 + b^2 = c^2 的三元组的个数
@timer
def force_three_sum(n):
    '''
    暴力求解
    '''
    res = 0
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                if a**2 + b**2 == c**2:
                    res += 1
    return res
