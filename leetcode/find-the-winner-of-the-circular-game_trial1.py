class Solution(object):
    def findTheWinner(self, n, k):
        def rec(n,k):
            if n==1:
                return 0
            return (rec(n-1,k)+k)%n
        return rec(n,k)+1

    # 1 2 3 4 5
    # 3 4 5 1
    # 5 1 3
    # 3 5
    # 3
    # 3  0
    # 3  0
    # 3  2
    # 3  0
    # 3  2