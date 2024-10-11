# 车道小车保持

# n 为车道上小车的数量
# input 为列表，保持 [位置，速度]

# 按照位置对 input 排序
input = sorted(input, key=lambda x: x[0])
n = len(input)
for i in range(n):

#一条单向单车道的道路上有n辆车，第 辆车位于 i，速度大小为 。
# 显然，如果车辆保持此速度行驶下去，在大多数情况下都会发生碰撞。
# 现在牛牛想知道，至少需要移除几辆车，才能让这些车不发生碰撞？  
# 
# 

# 移除部分元素，是的接下来的元素满足单调性 a1 <= a2 <= a3 <= ... <= an
# 保持速度，移除尽可能少的车辆
# 单调栈，维持从后往前遍历的单调递减栈
stack = []
res = 0
for i in range(n):
    while stack and stack[-1][1] > input[i][1]:
        res += 1
        stack.pop()
    stack.append(input[i])