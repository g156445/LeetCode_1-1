'''
思路：
    1. 将minSize到 maxSize之间所有的窗口输出，根据不同的窗口分成多个类
        1.1. 窗口分类过程中，子字符串使用counter与 .items()方法，统计列表中每个字符串出现的次数（重复的会自动叠加）
        1.2. 统计好后，使用counter计算每个子字符串的长度，用dict格式输出字母种类的长度，如：子字符串的长度 > maxLetters则删除
    2. 选出子串中出现次数最多的



'''
from collections import Counter

# class Solution:
#     def maxFreq(self, s, maxLetters, minSize, maxSize):




string_list = ["apple"]
letter_count = Counter(string_list)
print(letter_count)


# 遍历列表中的每个字符串，统计每个字符串中各字母的出现次数
string_list1 = ["apple"]
for s in string_list1:
    letter_count = Counter(s)
    print("字母计数:",dict(letter_count))


# 判断集合长度
dicta={"name":"zhangSan", "age":18, "hobby":"football"}
print(len(dicta))