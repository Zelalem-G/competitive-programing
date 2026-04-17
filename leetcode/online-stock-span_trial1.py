class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1

        while self.stack:

            last_price, last_span = self.stack[-1]

            if last_price > price:
                break

            self.stack.pop()

            span += last_span

        self.stack.append((price, span))

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)