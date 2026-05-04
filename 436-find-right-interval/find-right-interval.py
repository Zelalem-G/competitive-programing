class Solution(object):
    def findRightInterval(self, intervals):
        n = len(intervals)

        starts = sorted((intervals[i][0], i) for i in range(n))

        res = [-1] * n

        for i in range(n):
            end = intervals[i][1]

            l, r = 0, n
            while l < r:
                m = (l + r) // 2
                if starts[m][0] < end:
                    l = m + 1
                else:
                    r = m

            if l < n:
                res[i] = starts[l][1]

        return res