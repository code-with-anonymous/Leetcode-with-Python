from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        next = 1
        for now in range(len(nums) - 1):
            if nums[now] == nums[next]:
                nums[now] *= 2
                nums[next] = 0
                next += 1
            elif nums[now] != nums[next]:
                next += 1  
        
        # Moving non-zero elements to the front
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        
        print(nums)
        return nums

# Test
sol = Solution()
sol.applyOperations([1, 2, 2, 1, 1, 0])
