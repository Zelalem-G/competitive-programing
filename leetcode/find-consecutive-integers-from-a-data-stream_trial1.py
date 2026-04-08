class DataStream(object):

    def __init__(self, value, k):
        self.value = value
        self.k = k
        self.streak = 0
        

    def consec(self, num):
        if num == self.value:
            self.streak += 1
        else:
            self.streak = 0

        if self.streak >= self.k:
            return True
        else:
            return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)