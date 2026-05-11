class StockSpanner:

    def __init__(self):
        self.stack=[]
    def next(self, price: int) -> int:
        span=1
        while self.stack and price >=self.stack[-1][1]:
            prevSpan,prevPrice=self.stack.pop()
            span+=prevSpan
        self.stack.append((span,price))
        return span       


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)