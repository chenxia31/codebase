#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024年9月26日 10:47:39
# @Author  : chenlongxu
# @Mail    : xuchenlong796@qq.com
#
# 描述 ：  力扣 L221  最大正方形 找到只包含 1 的最大正方形，并返回其面积


# 分步骤进行求解
# 1. 首先需要考虑如何将状态记录下来，利用前缀和的方式来记录当前矩阵所有1 的数量
# 2，状态更新，如何考虑 1 的正方形，有一个性质是里面的和为 k*k 
# 3. 如何表示当前状态的转移

def maximalSquare(matrix):
    if not matrix:
        return 0 
    m,n = len(matrix), len(matrix[0])
    # 1. 初始化矩阵数组
    dp = [[int(x) for x in raw]for raw in matrix]

    # 2. 状态更新, dp[i][j] 表示以 i,j 为右下角的最大正方形的边长,那么状态转移方程为
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    print(dp)
    # 3. 最终的结果
    res = max(max(row) for row in dp)
    return res * res
    


matrix = [['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']]
print(maximalSquare(matrix))