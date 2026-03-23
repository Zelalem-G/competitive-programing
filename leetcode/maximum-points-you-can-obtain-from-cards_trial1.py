class Solution:
    def maxScore(self, cardPoints, k):
        cur = sum(cardPoints[:k])
        max_sum = cur
        
        for i in range(k):
            cur -= cardPoints[k-1-i]
            
            cur += cardPoints[-1-i]
            
            if cur > max_sum:
                max_sum = cur
                
        return max_sum