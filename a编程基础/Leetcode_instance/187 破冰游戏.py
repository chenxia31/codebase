#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024年9月26日 11:28:08
# @Author  : chenlongxu
# @Mail    : xuchenlong796@qq.com
#
# 描述 : 力扣 187 破冰游戏

# 社团中 num 成员围成一个圈开始游戏，抽取 target 来进行删除，每次删除第 target 个成员，然后从下一个成员开始继续游戏，求出最终剩下的成员
def lastRemaining(n, m):
    '''
    约瑟夫环问题
    '''
    res = 0
    for i in range(2, n+1):
        res = (res + m) % i
    return res

n = 5
m = 3
print(lastRemaining(n, m))