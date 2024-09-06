from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n  # Initialize result list with zeros
        stack = []  # Stack to store indices of temperatures
        
        for i in range(n):
            # Process each temperature
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()  # Pop the top of the stack
                result[idx] = i - idx  # Calculate the difference in days
            stack.append(i)  # Push current index onto the stack
        
        return result
