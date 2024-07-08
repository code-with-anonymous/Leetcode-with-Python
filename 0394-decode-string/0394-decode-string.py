class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        res = ""

        for c in s:
            if c.isdigit():
                curNum = curNum * 10 + int(c)
            elif c == "[":
                stack.append(res)
                stack.append(curNum)
                res = ""
                curNum = 0
            elif  c == "]":
                k = stack.pop()
                prev = stack.pop()
                res = prev + k * res
            else: 
                res += c
        return res
        