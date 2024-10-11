# 小红举办 PK，每个人战斗力 a 
# 自动划分两个队伍，使得两个队伍的战斗力最差绝对值最小

n = int(input())
a = list(map(int, input().split()))

# 例如 [7,4,5,3]其中一个队伍为[7,3]，另一个队伍为[4,5]
# 例如【1977,1,1】 其中一个队伍为[1977]，另一个队伍为[1,1]
# 例如 [1,3,4,2,3,6,9] 其中一个队伍为[1,3,4,6]，另一个队伍为[2,3,9]
a.sort(reverse=True)
team1 = 0
team2 = 0
# 从大到小遍历，分别放入两个队伍
for i in range(n):
    if team1 <= team2:
        team1 += a[i]
    else:
        team2 += a[i]
print(abs(team1 - team2))



# 用户详情页中加入年龄、IP 地址和 MCN 机构

# 从n个收藏夹中选出两个，让不同 MCN 的收藏夹机构数量恰好为 x
T = int(input())
for _ in range(T):
    n, x = map(int, input().split())
    res = []
    for _ in range(n):
        res.append(list(map(str, input().split())))
    # res[0] 为数量, res[1:] 为收藏夹详情
    # 现在需要找到两个收藏夹，使得不同MCN的收藏夹机构数量为x
    for i in range(n):
        for j in range(i+1, n):
            # 两个收藏夹的机构数量
            mcn = len(set(res[i][1:]) | set(res[j][1:]))
            if mcn == x:
                print(i+1, j+1)
                break
        

# 第三题
# 同学将 n 个座位成一个圈，m 个同学挑选各自喜欢的位置坐下
# 体育老师为大家送礼物，希望找到所有人到礼物的距离之和最小
# AC 27%
n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
res = [0] * n
# 遍历
for i in range(n):
    # 礼物放在第 i 位置需要的总距离为多少
    for j in range(m):
        res[i] += min(abs(a[j] - i), n - abs(a[j] - i))
# 最小距离对应的座位下标
print(res.index(min(res)) + 1)

# 如何降低上述第三题解法的时间复杂度

# 如何从座位的角度来推导出最小距离的礼物位置
# 例如 1 4 3 中，礼物放在 3 位置，总距离为 1 + 1 + 0 = 2
