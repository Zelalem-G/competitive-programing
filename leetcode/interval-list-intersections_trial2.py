class Solution(object):
    def intervalIntersection(self, a, b):
        ans = []
        i,j=0,0
        while i<len(a) and j<len(b):
            a1,a2=a[i]
            b1,b2=b[j]
            
            if max(a1, b1) <= min(a2, b2):
                ans.append([max(a1, b1), min(a2, b2)])
            if b2<a2:
                j += 1
            else:
                i += 1


        return ans