class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        values={'}':'{',']':'[',')':'('}
        for i in s :
            if i in values:
                if stack and stack[-1]==values[i]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(i)
        return not stack