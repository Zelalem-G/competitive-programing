from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)
        r = t-3000
        while self.requests[0]<r:
            self.requests.popleft()
        return len(self.requests)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)