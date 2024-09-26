# 小美给自己物品贴标签, m中标签，每个标签只有 1 次
# 每个物品对应一种标签 A(1*n),每一个对应的标签数量
# 贴标签之后，美观度为 B(1*n)
# 补贴标签，美观度为 C(1*n)
# 问最大美观度

# 输入
n = 3
m = 3
A = [1, 2, 1]
B = [5,4,3]
C = [-1,2,-100]

# 输出
# 6

baseline = sum(C)
uplift = [B[i] - C[i] for i in range(n)] # 每个的提升
# 计算每种标签下的最大提升

temp_index = set(A)
for i in temp_index:
    # 适合第 i 标签的物品有哪些
    items = [j for j in range(n) if A[j] == i+1]
    # 找到最大的提升
    if items:
        baseline += max([uplift[j] for j in items])
print(baseline)


# 无限大的二维平面
# 平面 n 个地雷，第 i 个地雷在 (x[i], y[i])
# 在ti时刻会发生爆炸
# 引爆 ki 个地雷，爆炸范围是所有地雷的曼哈顿距离不超过 ki 的地雷
# 问最早引爆所有地雷的时间

T = 1
n = 3 # 地雷个数
m = 3 # 至少需要引爆的地雷个数
# x,y,t,k
bomb = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
# 输出
# 3

def manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

# bomb 按照引爆时间排序
bomb.sort(key=lambda x:x[2])

# 计算地雷之间的曼哈顿距离
dist = [[0]*n for _ in range(n)]
for q in range(n):
    for w in range(q+1, n):
        dist[q][w] = manhattan(bomb[q][0], bomb[q][1],bomb[w][0], bomb[w][1])
        dist[w][q] = dist[q][w]

# 模拟找到引爆 m 地雷的时间
min_time = 0
while m > 0:
    temp = bomb.pop(0)
    m -= 1
    # 找到所有地雷的曼哈顿距离,设置时间
    for i in range(len(bomb)):
        if dist[i][0] <= temp[3]:
            # 说明会被引爆
            bomb[i][2] = 0
    bomb.sort(key=lambda x:x[2])
    while bomb and bomb[0][2] == 0:
        bomb.pop(0)
        m -= 1
    min_time = temp[2]
print(temp[2])
