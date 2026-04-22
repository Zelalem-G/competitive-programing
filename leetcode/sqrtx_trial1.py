class Solution(object):
    def mySqrt(self, x):
        l=0
        r=(x//2)+1

        while l<=r:
            m = (l + r) // 2
            p= m*m
            if p<x:
                l=m+1
            elif p>x:
                r=m-1
            else:
                return m

        
        return r
