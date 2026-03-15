class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        points.sort(key=lambda x:(x[0]))
        ans = 0

        for p in range(1,len(points)):
            d = points[p][0]-points[p-1][0]
            ans = max(ans,d)
        
        return ans
        