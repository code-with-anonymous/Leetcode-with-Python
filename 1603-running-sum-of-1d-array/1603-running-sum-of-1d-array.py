class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        arr = []
        for i in nums:
            sum = sum + i
            arr.append(sum)
        return arr