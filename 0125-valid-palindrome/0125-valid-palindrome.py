# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         x = ''.join(char for char in s if char.isalnum())
#         x = x.lower()
#         return x == x[::-1]        
#    ]     

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True






