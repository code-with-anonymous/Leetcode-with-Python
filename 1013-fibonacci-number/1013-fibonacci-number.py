class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        a, b = 0, 1
        
        for i in range(2, n + 1):  # Loop range should include n
            a, b = b, a + b  # Correctly update a and b simultaneously
        
        return b  # Return the nth Fibonacci number
