class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        array = []
        spaces_lf = 0 
        for i in range(len(s)):
            if spaces_lf < len(spaces) and i == spaces[spaces_lf]:
                array.append(" ")
                spaces_lf += 1
            array.append(s[i])
        return "".join(array)    