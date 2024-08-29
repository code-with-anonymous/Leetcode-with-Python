class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # result = []
        # for i in range(len(accounts)):
        #     add=sum(accounts[i])
        #     result.append(add)

        # maximum=max(result)
        # return maximum  

        # optimizing i by using o(1) space cmplexity and o(n*n) time complexity 
        # optimizing the code by using no extra space and updating variable for maximum wealth
        wealth =sum(accounts[0])
        for i in range(1,len(accounts)):
            addition=sum(accounts[i])
            if addition > wealth:
                wealth =addition
        return wealth        