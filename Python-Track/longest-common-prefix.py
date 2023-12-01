class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        strs.sort(key=lambda x:len(x))
        for i in range(len(strs[0])):
            for j in range (len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                    return result
            else:
                result+=strs[0][i]
        return result
            







        