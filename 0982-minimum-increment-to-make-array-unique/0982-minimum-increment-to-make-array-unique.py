from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                increment = nums[i-1] - nums[i] + 1
                moves += increment
                nums[i] += increment
        
        return moves
     