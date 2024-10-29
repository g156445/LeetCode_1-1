class Solution:
    def maxSum(self, nums, m, k):
        # 获取所有符合长度为 k 且不同元素数目 >= m 的子数组
        valid_subarrays = list(self.all_list(nums, m, k))
        max_substring = 0

        # 如果找到符合条件的子数组，计算其最大和
        if valid_subarrays:
            for subarray in valid_subarrays:
                max_substring = max(max_substring, sum(subarray))
        else:
            max_substring = 0  # 若无符合条件的子数组，则返回 0
        return max_substring

    def all_list(self, nums, m, k):
        unique_substr = set()
        for location in range(len(nums) - k + 1):
            subarray = tuple(nums[location: location + k])  # 转换为 tuple 以便加入集合
            if len(set(subarray)) >= m:  # 检查子数组是否有至少 m 个不同元素
                unique_substr.add(subarray)
        return unique_substr

# test part:
solution = Solution()

nums = [1,2,1,2,1,2,1]
m = 3
k = 3

output = solution.maxSum(nums, m, k)
print((output))
