class Solution(object):
    def clearDigits(self, s):
        stack = []

        for c in s:
            if stack and c.isdigit():
                stack.pop()
            else:
                stack.append(c)
            
        return "".join(stack)
        