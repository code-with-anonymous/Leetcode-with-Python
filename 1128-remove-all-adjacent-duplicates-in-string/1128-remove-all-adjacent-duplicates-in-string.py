class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)

        #Explanation
#Initialize an empty stack: stack = []
#Iterate through each character of the string:
#If the stack is not empty and the top of the stack (stack[-1]) is equal to the current character (char), remove the top of the stack (stack.pop()).
#Otherwise, push the current character onto the stack (stack.append(char)).
#Build the final string: After processing all characters, the stack will contain the final string without any adjacent duplicates. Convert the stack to a string using ''.join(stack) and return it.



