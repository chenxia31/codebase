class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 状态：当前下标的丑数
        # 转移：记录用过的质因数下标是多少
        # dp[i+1] = min(dp[k2]*2,dp[k3]*3,dp[k5]*5)
        dp =[0] * (n+1)
        dp[1] = 1
        p2 = p3 = p5 = 1
        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        
        return dp[n]

n = 10
s = Solution()
print(s.nthUglyNumber(n))