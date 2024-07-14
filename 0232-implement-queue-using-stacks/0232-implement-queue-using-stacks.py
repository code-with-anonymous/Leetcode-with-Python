# class MyQueue:

#     def __init__(self):
#         self.stack1=[]
#         self.stack2=[]
        

#     def push(self, x: int) -> None:
#         self.stack1.append(x)

        

#     def pop(self) -> int:
#         for i in range(1, len(self.stack1)):
#             if self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         popped =self.stack1.pop()  
#         for i in self.stack2:
#              self.stack1.append(self.stack2.pop()) 
#         return popped         
        

#     def peek(self) -> int:
#         return self.stack1[0]

#     def empty(self) -> bool:
#         return not self.stack1
        
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:  # Only move elements if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:  # Only move elements if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()