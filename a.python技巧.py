
'''

技巧：  1 << k
    1 << k  是左移运算，即将数字 1 向左移动 k 位
    左移 k 位相当于乘以 2^k。比如
        1 << 2  表示将 1 左移 2 位，结果是 4，因为 1 × 2^2 =4
        1 << 3  表示将 1 左移 3 位，结果是 8，因为 1 × 2^3 =8


技巧：  2**k
    2**k 是 2 的 k 次方
    2**2 是 2 的 2 次方


技巧：  set()
    set() 是 Python 中的集合类型，是一个 不包含重复元素 且 无序的数据结构。
    seen = set() 表示初始化了一个空集合 seen。集合可以存储独特的值，常用于去重或判断某个元素是否已经出现过。


技巧：  seen.add(substring)
    add() 方法用于向集合 seen 中添加元素。
        seen.add(substring) 表示将 substring 这个子串添加到集合 seen 中。
        如果 substring 已经在集合中，集合会自动避免重复。


技巧：  Counter    elements()
    s1 = ['00', '01', '11', '01', '11', '10']   s2 = ['00', '01', '11']
    Counter会计算每个元素的出现次数   (counter1 - counter2 会将 s1 中与 s2 重复的元素按出现次数相减，保留剩下的元素)
        counter1 = Counter(s1)
        counter2 = Counter(s2)

    .elements() 将剩余的元素还原为列表
    list((counter1 - counter2).elements())


技巧：  format(i, f'0{k}b')
    format(i, f'0{k}b') 是将整数 i 转换为长度为 k 的二进制字符串。
    f'0{k}b' 是格式化字符串：
        0{k} 表示字符串的长度为 k 位，并且如果不够长，会在前面补 0。
        b    表示转换为二进制。


组合技巧：   2**k/ 1<<k 与 format(i, f'0{k}b')结合
        结合使用，通常用于遍历 k 位二进制数的所有可能组合
            比如： for i in range(8):
                     print(format(i, f'03b'))    #k=3
                     输出：000，001，010，011，100，101，110，111


技巧：  zip 列表、元组、字符串会逐一配对，生成一个包含元组的迭代器（忽略较长序列的多余元素）
        (合并)用例：  list1 = [1, 2, 3]   list2 = ['a', 'b', 'c']   zipped = zip(list1, list2)
                     print(list(zipped))
                    =>   [(1, 'a'), (2, 'b'), (3, 'c')]

        (解压)用例：  pairs = [('x', 1), ('y', 2), ('z', 3)]     letters, numbers = zip(*pairs)
                     print(letters)         =>   ('x', 'y', 'z')
                     print(numbers)         =>   (1, 2, 3)

        (键值对)(字典)用例：  keys = ['name', 'age', 'gender']      values = ['Alice', 25, 'Female']    dictionary = dict(zip(keys, values))
                            print(dictionary)
                            =>   {'name': 'Alice', 'age': 25, 'gender': 'Female'}


技巧：  ”首尾相连“ 的窗口
        解法：优先从列表的尾部开始计算
            比如： 计算窗口为 k 的最大合时：
                   a = sum(cardPoints[-k:])
                   cardPoints[-k:] 提取列表的最后 k 个元素，这样直接计算边界的窗口元素，不需要考虑列表起始位置，代码简洁高效


技巧：  字典出现的最多key的次数
        解法：用 max() 函数结合 Counter 字典的值
            比如： from collections import Counter
                  windows_count = {'aab': 2, 'aba': 1, 'bab': 1, 'caa': 1, 'aaba': 1, 'abab': 1}

                  # 找到出现次数最多的子字符串及其次数
                  max_substring = max(windows_count, key=windows_count.get)  # 获取出现次数最多的子字符串
                  max_count = windows_count[max_substring]  # 获取该子字符串的出现次数
                  print(f"出现次数最多的子字符串是 '{max_substring}'，次数为 {max_count}")

                解释： max(windows_count, key=windows_count.get)：找到字典中值最大的键，也就是出现次数最多的子字符串。
                      windows_count[max_substring]：查找该子字符串对应的出现次数。


技巧：   sorted() 方法可将List从小到大排序
            比如： numbers = [5, 3, 8, 1, 9]
                  sorted_numbers = sorted(numbers)
                  print(sorted_numbers)



'''