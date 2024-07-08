#  class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []
#         curNum = 0
#         res = ""

#         for c in s:
#             if c.isdigit():
#                 curNum = curNum * 10 + int(c)
#             elif c == "[":
#                 stack.append(res)
#                 stack.append(curNum)
#                 res = ""
#                 curNum = 0
#             elif  c == "]":
#                 k = stack.pop()
#                 prev = stack.pop()
#                 res = prev + k * res
#             else: 
#                 res += c
#         return res
        
class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        string_stack = []
        k = 0

        for c in s:
            if c.isdigit():
                k = (k * 10) + int(c)
                continue

            if c == '[':
                num_stack.append(k)
                k = 0
                string_stack.append(c)
                continue

            if c != ']':
                string_stack.append(c)
                continue

            temp = []
            while string_stack[-1] != '[':
                temp.insert(0, string_stack.pop())

            # remove the "["
            string_stack.pop()

            # Get the new string
            replacement = ''.join(temp) * num_stack.pop()

            # Add it to the stack
            string_stack.append(replacement)

        result = ''.join(string_stack)
        return result
        