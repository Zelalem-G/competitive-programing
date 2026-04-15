class Solution(object):
    def getRow(self, r):
        if r == 0:
            return [1]
        
        prev = self.getRow(r-1)
        new = [1]

        for i in range(1, len(prev)):
            new.append(prev[i-1] + prev[i])
        
        new.append(1)
        return new