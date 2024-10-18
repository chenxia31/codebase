'''
给一个二进制数组 nums 

可以对数组执行以下操作 任意次（也可以是 0 次）
- 选择数组中任意连续三个元素进行反转，从 0 变成 1 ，从 1 变成 0

返回将 nums 中的所有元素变成 1 所需要的最小操作数


数字相关的标签包括：
- 位运算
- 队列
- 数组
- 前缀和
- 滑动窗口

提示 1 如果第一个元素是 0 ，那么我们可以直接将前三个元素反转
提示 2 之后可以使用相同的思路来进行
'''

def minOperatuibs(nums):
    '''
    input: nums: List[int]
        [0,1,1,1,0,0]
    '''
    res = 0
    while nums:
        temp = nums.pop(0)
        if temp == 0:
            res += 1 # 必然需要反转
            if len(nums) == 0:
                return res
            if len(nums) == 1:
                nums[0] = 1 - nums[0]
            if len(nums) >= 2:
                nums[0] = 1 - nums[0]
                nums[1] = 1 - nums[1]
    return res 

nums = [0,1,1,1,0,0]    
print(minOperatuibs(nums)) # 3

            