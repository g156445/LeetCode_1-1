'''
思路：
    1. 将minSize到 maxSize之间所有的窗口输出，根据不同的窗口分成多个类
        1.1. 窗口分类过程中，子字符串使用counter方法，统计列表中每个字符串的次数（重复的会自动叠加）
        1.2. 用counter计算每个子字符串的长度，用dict格式输出字母种类的长度，如：子字符串的长度 > maxLetters则删除
    2. 选出子串中出现次数最多的

'''
from collections import Counter

class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        string_list = []
        # 外层循环控制窗口大小的增量，表示从 minSize 到 maxSize 的变化
        for windows_move_location in range(maxSize - minSize + 1):
            # 内层循环滑动窗口，逐个生成子字符串
            for location in range(len(s) - (minSize + windows_move_location) + 1):
                substring = s[location: location + minSize + windows_move_location]  # 提取当前窗口的子字符串
                letter_count = Counter(substring)  # 统计当前窗口子字符串中每个字母的出现次数

                # 如果当前窗口中的不同字母种类小于等于 maxLetters，则添加到结果列表
                if len(letter_count) <= maxLetters:
                    string_list.append(substring)

        # 对符合条件的窗口子字符串进行计数
        windows_count = Counter(string_list)

        # 检查是否有符合条件的子字符串
        if not windows_count:
            print("没有符合条件的子字符串。")
            return 0  # 或者返回其他合适的值

        # 找到出现次数最多的子字符串及其次数
        max_substring = max(windows_count, key=windows_count.get)  # 获取出现次数最多的子字符串
        max_count = windows_count[max_substring]  # 获取该子字符串的出现次数
        print(f"出现次数最多的子字符串是 '{max_substring}'，次数为 {max_count}")

        return max_count
s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4

string_list = []
# 外层循环控制窗口大小的增量，表示从 minSize 到 maxSize 的变化
for windows_move_location in range(maxSize - minSize + 1):  # 意味着 maxSize - minSize + 1, 循环 2 次 (minSize, maxSize)

    # 内层循环滑动窗口，逐个生成子字符串
    for location in range(len(s) - (minSize + windows_move_location) + 1):
        substring = s[location: location + minSize + windows_move_location]  # 提取当前窗口的子字符串
        letter_count = Counter(substring)  # 统计当前窗口子字符串中每个字母的出现次数

        # 如果当前窗口中的不同字母种类小于等于 maxLetters，则添加到结果列表
        if len(letter_count) <= maxLetters:
            string_list.append(substring)


# 对符合条件的窗口子字符串进行计数
windows_count = Counter(string_list)
print("windows_count:", dict(windows_count))  # 输出结果，显示各子字符串的出现次数

# 找到出现次数最多的子字符串及其次数
max_substring = max(windows_count, key=windows_count.get)  # 获取出现次数最多的子字符串
max_count = windows_count[max_substring]  # 获取该子字符串的出现次数
print(f"出现次数最多的子字符串是 '{max_substring}'，次数为 {max_count}")

print("-------------正式跑一下--------------------")

solution = Solution()
print(solution.maxFreq(s, maxLetters, minSize, maxSize))

print("-------------------------------------------")

string_list = ["apple", "apple"]
letter_count = Counter(string_list)
print(letter_count)

# 遍历列表中的每个字符串，统计每个字符串中各字母的出现次数
string_list1 = ["apple"]
for s in string_list1:
    letter_count = Counter(s)
print("字母计数:", dict(letter_count))

# 判断集合长度
dicta = {"name": "zhangSan", "age": 18, "hobby": "football"}
print(len(dicta))
