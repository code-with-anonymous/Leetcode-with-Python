class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums)//3
        ls = []
        count1 , count2 , element1 , element2 = 0 , 0 , 0 , 0
        for i in nums:
            if count1 == 0 and i != element2:
                count1 = 1
                element1 = i
            elif count2==0 and i != element1:
                count2 = 1
                element2 = i
            elif i == element1:
                count1+=1
            elif i == element2:
                count2+=1
            else:
                count1-=1
                count2-=1
                
        count1,count2 = 0,0
        for i in nums:
            if i == element1:
                count1+=1
            elif i == element2:
                count2+=1
        if count1>size:
            ls.append(element1)
        if count2>size:
            ls.append(element2)
        return ls