class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in dic:  # if char is a closing bracket
                if stack and stack[-1] == dic[char]:
                    stack.pop()
                else:
                    return False
            else:  # if char is an opening bracket
                stack.append(char)
        return not stack  # returns True if stack is empty, otherwise False
       