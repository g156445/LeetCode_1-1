from collections import Counter
'''
问题：代码时间超出问题是因为对于较大的输入 s，枚举所有可能的长度为 k 的二进制字符串（2^k 个），
    并且使用 Counter 进行差集计算是非常耗时的。我们可以使用更高效的方法，避免生成所有的二进制字符串，从而减少时间复杂度
'''
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        all_substr = self.generate_binary_strings(k)
        extract_substr = self.extract_substring(s, k)
        all_substr1 = Counter(all_substr)
        extract_substr1 = Counter(extract_substr)
        result = list((all_substr1 - extract_substr1).elements())

        if len(result) == 0:
            hasAllCode = True
        else:
            hasAllCode = False

        return hasAllCode


    def generate_binary_strings(self, k):
        # 生成从 0 到 2^k - 1 的所有整数，并将其转换为长度为 k 的二进制字符串
        result = [format(i, f'0{k}b') for i in range(2 ** k)]
        # 结果: ['000', '001', '010', '011', '100', '101', '110', '111']
        return result

    def extract_substring(self, s, k):
        bulk = []
        for location in range(len(s) - k + 1):
            if s[location:location+k] in bulk:
                continue
            else:
                bulk.append(s[location:location+k])
        return bulk


'''
优化后的代码
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 需要的不同长度为 k 的二进制字符串的数量
        need = 1 << k  # 相当于 2^k
        seen = set()

        # 遍历字符串 s，提取所有长度为 k 的子串
        for i in range(len(s) - k + 1):
            substring = s[i:i + k]
            seen.add(substring)

            # 一旦收集到足够的子字符串，就可以提前返回 True
            if len(seen) == need:
                return True

        # 如果遍历结束仍没有收集到所有可能的子字符串，返回 False
        return False
'''

'''
技巧1：  1 << k 
    1 << k  是左移运算，即将数字 1 向左移动 k 位
    左移 k 位相当于乘以 2^k。比如
        1 << 2  表示将 1 左移 2 位，结果是 4，因为 1 × 2^2 =4
        1 << 3  表示将 1 左移 3 位，结果是 8，因为 1 × 2^3 =8
        
技巧2:    set()
    set() 是 Python 中的集合类型，是一个 不包含重复元素 且 无序的数据结构。
    seen = set() 表示初始化了一个空集合 seen。集合可以存储独特的值，常用于去重或判断某个元素是否已经出现过。
    
技巧3：  seen.add(substring)
    add() 方法用于向集合 seen 中添加元素。
        seen.add(substring) 表示将 substring 这个子串添加到集合 seen 中。
        如果 substring 已经在集合中，集合会自动避免重复。

'''