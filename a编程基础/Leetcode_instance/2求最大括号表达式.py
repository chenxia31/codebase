'''
有效表达式的定义 

空字符串和括号均是有效的表达式
当 AB 为有效表达式的时候，(A)B 和 AB 都是有效表达式

括号表达式的值
'''
def maxExpression(s):
    # 递归结束条件
    if s == "":
        return 0
    if len(s) == 1:
        return 1
    # 递归
    res = 0
    for i in range(1, len(s)):
        res = max(res, maxExpression(s[:i]) + maxExpression(s[i:]))
    return res