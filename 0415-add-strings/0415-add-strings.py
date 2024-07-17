class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        carry = 0
        # Initialize two pointers to the end of num1 and num2
        i, j = len(num1) - 1, len(num2) - 1

        # Loop through num1 and num2 from right to left
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
                j -= 1
            result = chr(carry % 10 + ord('0')) + result
            carry //= 10

        return result
        