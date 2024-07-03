class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set= set(nums)
        for i in num_set:
            if not (i-1) in num_set:
                count = 1
                while i+count in num_set:
                    count +=1
                longest=max(longest, count)      
        return longest      

        