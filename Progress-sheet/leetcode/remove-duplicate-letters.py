class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        ch = Counter(s)

        stack = []

        for i in range(len(s)):
            while stack and stack[-1] >= s[i] and ch[stack[-1]] > 1 and (s[i] not in seen):
                temp = stack.pop()
                ch[temp] -= 1
                seen.remove(temp)
    
            if s[i] not in seen:
                stack.append(s[i])
                seen.add(s[i])
            else:
                ch[s[i]] -= 1
        

        return ''.join(stack)