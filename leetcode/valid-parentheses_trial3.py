class Solution(object):
    def isValid(self, s):
        bracket = {}
        bracket["["] = "]"
        bracket["{"] = "}"
        bracket["("] = ")"

        stack = []
        for c in s:
            if c in bracket:
                stack.append(c)
            else:
                if stack and bracket[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        if len(stack)==0:
            return True
        else:
            return False