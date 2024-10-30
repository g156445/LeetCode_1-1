class Solution:
    def maximumSubarraySum(self, nums, k):
        # 生成所有的长度为k的窗口
        create_windows_No_deal = self.create_windows_No_deal(nums, k)
        # 处理窗口，保留符合条件的窗口和清零不符合条件的窗口
        windows_deal = self.windows_deal(create_windows_No_deal)
        max_subarray_sum = 0
        for location in range(len(windows_deal)):
            if windows_deal[location] != 0:  # 确保只计算非零窗口
                max_subarray_sum = max(max_subarray_sum, sum(windows_deal[location]))
        return max_subarray_sum

    def create_windows_No_deal(self, nums, k):
        windows_No_deal = []
        for location in range(len(nums) - k + 1):
            windows_No_deal.append(nums[location: location + k])
        return windows_No_deal

    def windows_deal(self, create_windows_No_deal):
        for location in range(len(create_windows_No_deal)):
            seen = set()
            for substring in create_windows_No_deal[location]:  # 迭代子数组的每个元素
                seen.add(substring)
            # 如果该子数组的唯一元素数量不等于子数组长度 k，将子数组替换为 0
            if len(seen) != len(create_windows_No_deal[location]):
                create_windows_No_deal[location] = 0
        return create_windows_No_deal


solution = Solution()

nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
print(solution.maximumSubarraySum(nums, k))
