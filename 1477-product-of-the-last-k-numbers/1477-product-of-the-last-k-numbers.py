class ProductOfNumbers:

    def __init__(self):
        self.queue = deque()
        self.countOfOne = 0

    def add(self, num: int) -> None:
        self.queue.append(num)
        if (num == 1):
            self.countOfOne += 1

    def getProduct(self, k: int) -> int:
        if (self.countOfOne == len(self.queue)):
            return 1
        else:
            product = 1
            lst = []
            while (k > 0):
                q = self.queue.pop()
                product *= q
                lst.append(q)
                k -= 1
            lst = lst[::-1]
            for i in lst:
                self.queue.append(i)
            return product
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)