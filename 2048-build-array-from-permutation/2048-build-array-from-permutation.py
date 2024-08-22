from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)  # Initialize the list with the same length as nums
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans  # Return the correct list
 