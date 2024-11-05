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