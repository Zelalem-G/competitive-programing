class Solution:
    def minimumRecolors(self, blocks, k):
        ans = k
        l=0
        count = 0
        for r in range(len(blocks)):
            if blocks[r] == "W":
                count += 1
            if (r-l+1) == k:
                ans = min(count,ans)
                if blocks[l] == "W":
                    count -= 1
                l += 1

        return ans