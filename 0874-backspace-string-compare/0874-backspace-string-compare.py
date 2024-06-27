
        # stack=[]
        # for i in s:
        #    if stack and i =='#' :
        #           stack.pop()
        #    else:
        #           stack.append(i)
        # stack=(''.join(stack))  

        # stack1=[]
        # for i in t:
        #    if stack1 and i =='#' :
        #           stack1.pop()
        #    else:
        #           stack1.append(i)
        # stack1=''.join(stack1)       
        # if stack1 == stack1:
        #     return True
        # else:
        #     return False    

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def processString(string):
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return ''.join(stack)
        
        return processString(s) == processString(t)
        



        
        
        
# Explanation:
# Class Definition:

# class Solution:: Defines a new class named Solution.
# Method Definition:

# def backspaceCompare(self, s: str, t: str) -> bool:: Defines a method named backspaceCompare which takes two string arguments s and t, and returns a boolean.
# Helper Function:

# def processString(string):: A helper function within backspaceCompare that processes a string to simulate backspaces using a stack.
# It iterates over each character in the string. If the character is #, it pops from the stack (if the stack is not empty). Otherwise, it appends the character to the stack.
# The helper function returns the final state of the stack as a single string.
# Comparison:

# return processString(s) == processString(t): Compares the processed versions of s and t. If they are equal, it returns True; otherwise, it returns False.
        