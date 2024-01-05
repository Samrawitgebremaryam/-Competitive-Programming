class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newset=set()
        l=0
        result=0
        for r in range(len(s)):
            while s[r] in newset:
                newset.remove(s[l])
                l+=1
            newset.add(s[r])
            result=max(result,r-l+1)
        return result
















        # num = []
        # l = 0
        # for i in range(len(s)):
        #     num.append(s[i])
        #     if len(num) == len(set(num)) and len(num) > l:
        #         l = len(num)
        #     else:
        #         while len(num) != len(set(num)):
        #             del num[0]
        # return l