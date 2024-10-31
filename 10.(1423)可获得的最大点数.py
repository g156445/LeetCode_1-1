class Solution:
    def maxScore(self, cardPoints, k):
        current_score = sum(cardPoints[-k:])
        max_score = current_score
        for location in range(k):
            current_score += cardPoints[location] - cardPoints[-k + location]
            max_score = max(max_score, current_score)
        return max_score


cardPoints = [1,2,3,4,5,6,1]
k = 3


solution = Solution()
print(solution.maxScore(cardPoints, k))