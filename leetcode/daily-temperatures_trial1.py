class Solution(object):
    def dailyTemperatures(self, temp):
        ans = [0]*len(temp)
        stack = []

        for i in range(len(temp)-1,-1,-1):
            while stack and temp[stack[-1]]<=temp[i]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1]-i
            else:
                ans[i] = 0
            stack.append(i)


        return ans