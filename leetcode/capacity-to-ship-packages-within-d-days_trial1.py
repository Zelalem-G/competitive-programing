class Solution(object):
    def shipWithinDays(self, weights, days):
        def can(c):
            cur=0
            d=1
            for w in weights:
                if cur + w > c:
                    cur=0
                    d+=1
                cur += w
            if d>days:
                return False
            else:
                return True

        l=max(weights)
        r=sum(weights)

        while l<r:
            m=l+(r-l)//2

            if can(m):
                r=m
            else:
                l=m+1
        
        return r
