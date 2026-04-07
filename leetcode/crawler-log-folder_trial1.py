class Solution(object):
    def minOperations(self, logs):
        stack = []

        for op in logs:
            if stack and op == "../":
                stack.pop()
            elif (len(stack)==0 and op == "../") or op == "./":
                continue
            else:
                stack.append(op)

        return len(stack)
        