"""
给你一个长度为 n 的整数数组 nums ，请你求出每个长度为 k 的子数组的 美丽值
一个子数组的 美丽值 定义为：如果子数组中第 x 小整数 是 负数 ，那么美丽值为第 x 小的数，否则美丽值为 0
请你返回一个包含 n - k + 1 个整数的数组，依次 表示数组中从第一个下标开始，每个长度为 k 的子数组的 美丽值
子数组指的是数组中一段连续 非空 的元素序列
"""


class Solution:
    def getSubarrayBeauty(self, nums, k, x):
        sub_string = []
        for location in range(len(nums) - k + 1):
            un_sorted_list = sorted(nums[location: k + location])
            if un_sorted_list[x - 1] < 0:
                sub_string.append(un_sorted_list[x - 1])
            else:
                sub_string.append(0)
        return sub_string

solution = Solution()

nums = [1,-1,-3,-2,3]
k = 3
x = 2

print(solution.getSubarrayBeauty(nums, k, x))
print("------------------------------------------------------")


"""
1. 初始化一个滑动窗口，并记录窗口内的负数及其频率。
2. 滑动窗口：每次移除窗口左侧的一个元素，加入窗口右侧的一个新元素。
3. 更新窗口负数的频率计数。
4. 查找当前窗口中第 x 小的负数，将其添加到结果列表 sub_string 中。
5. 如果找不到第 x 小的负数，添加 0 到 sub_string 中。
"""

from collections import deque, Counter


class Solution:
    def getSubarrayBeauty(self, nums, k, x):
        sub_string = []  # 用于存储每个窗口的第 x 小负数
        window = deque()  # 用于存储当前窗口内的元素
        negative_count = Counter()  # 记录窗口内负数的频率

        # 初始化第一个窗口
        for i in range(k):
            window.append(nums[i])  # 将前 k 个元素加入窗口
            if nums[i] < 0:
                negative_count[nums[i]] += 1  # 记录负数频率

        # 辅助函数：查找当前窗口内第 x 小的负数
        def find_xth_negative(x):
            count = 0
            # 按照负数从小到大遍历频率计数器
            for num in sorted(negative_count):
                count += negative_count[num]
                if count >= x:
                    return num  # 找到第 x 小负数
            return 0  # 如果不存在第 x 小负数，则返回 0

        # 将第一个窗口的结果加入 sub_string
        sub_string.append(find_xth_negative(x))

        # 开始滑动窗口
        for i in range(k, len(nums)):
            # 移出窗口左侧的元素
            left = window.popleft()
            if left < 0:
                negative_count[left] -= 1  # 更新负数频率计数
                if negative_count[left] == 0:
                    del negative_count[left]  # 删除频率为 0 的负数

            # 将新元素加入窗口右侧
            window.append(nums[i])
            if nums[i] < 0:
                negative_count[nums[i]] += 1  # 更新新负数的频率

            # 查找当前窗口的第 x 小负数并加入结果集
            sub_string.append(find_xth_negative(x))

        return sub_string  # 返回所有窗口的第 x 小负数


# 示例调用
solution = Solution()
nums = [1, -1, -3, -2, 3] * 2000  # 示例大数组
k = 4416
x = 2217

print(solution.getSubarrayBeauty(nums, k, x))


