# LeetCode_1-1  
滑动窗口与双指针- 1.定长  
**定长滑窗套路**  
总结成三步：**入-更新-出**  

>1. 入：下标为 i 的元素进入窗口，更新相关统计量。如果 i<k−1 则重复第一步。  
>2. 更新：更新答案。一般是更新最大值/最小值。  
>3. 出：下标为 i−k+1 的元素离开窗口，更新相关统计量。

以上三步适用于所有定长滑窗题目  
