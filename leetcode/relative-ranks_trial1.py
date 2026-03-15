class Solution(object):
    def findRelativeRanks(self, score):
        ans = [0]*len(score)

        count = [0]*(max(score)+1)
        for s in score:
            count[s] = 1
        
        rank = len(score)
        for c in range(len(count)):
            if count[c] == 1:
                if rank >3:
                    count[c] = str(rank)
                else:
                    if rank == 3:
                        count[c] = "Bronze Medal"
                    elif rank == 2:
                        count[c] = "Silver Medal"
                    else:
                        count[c] = "Gold Medal"
                rank -= 1
        
        for i in range(len(ans)):
            ans[i] = count[score[i]]

        return ans
