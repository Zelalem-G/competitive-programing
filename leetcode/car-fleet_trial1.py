class Solution(object):
    def carFleet(self, target, position, speed):
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)  
        stack = []

        for p, s in pairs:
            time = (target - p) / float(s) 
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)