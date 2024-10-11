# 如何实现编辑距离的计算

# 核心是用动态规划的方式来进行求解
# dp[i][j] 表示为：从 word 1 中第 i 个数组到 word2 中前 j 字符串之间的距离
# 初始化：dp[0] 全部为 n 
# 状态转移：dp[i][j] = min()

word1 = 'horse'
word2 = 'ros'

# 对于每个部门的操作包括：删除、替换和插入新的字符
m = len(word1)
n = len(word2)
dp = [[0]*(n+1) for _ in range(m+1) ]

for i in range(n+1):
    dp[0][i] = i 
for j in range(m+1):
    dp[j][0] = j

for i in range(1,m+1):
    for j in range(1,n+1):
        # 状态转移，根据判断是否相等来完成更新
        if word1[i-1] == word2[j-1]:
            # 两个相等说明不需要增加新的操作
            # 或者存在某种更小的计算方式
            dp[i][j] = min(dp[i-1][j-1]-1,dp[i-1][j],dp[i][j-1]) + 1
        else:
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
# 表示从 word1 中前 m 字母转换成为 word2 中前 n 字母需要编辑的距离
print(dp[m][n])
