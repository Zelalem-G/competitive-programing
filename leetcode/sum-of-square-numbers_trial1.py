class Solution(object):
    def judgeSquareSum(self, c):
        l=0
        r=math.floor(sqrt(c))

        while l<=r:
            n = l*l + r*r
            if n> c:
                r-=1
            elif n<c:
                l+=1
            else:
                return True

        return False