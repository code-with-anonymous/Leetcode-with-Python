from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        First find the breakpoint: nums[i] < nums[i+1]
        Second step is to find a number just greater than the breakpoint
        Third step is to reverse the remaining part
        """
        n = len(nums)
        index = -1

        # Step 1: Find the first index `i` such that nums[i] < nums[i + 1] from the end
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        if index == -1:
            # If no such index is found, the list is in descending order, reverse it to get the smallest permutation
            nums.reverse()
        else:
            # Step 2: Find the first index `j` from the end such that nums[j] > nums[index]
            for j in range(n - 1, index, -1):
                if nums[j] > nums[index]:
                    # Swap elements at `index` and `j`
                    nums[index], nums[j] = nums[j], nums[index]
                    break
            
            # Step 3: Reverse the sequence from index + 1 to the end of the list
            nums[index + 1:] = reversed(nums[index + 1:])
