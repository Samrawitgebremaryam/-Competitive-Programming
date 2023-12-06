class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=''
        minimum=min(len(word1),len(word2))
        for i in range (minimum):
            merged+=word1[i]+word2[i]
        if len(word1)>len(word2):
            merged+=word1[minimum:]
        else:
            merged+=word2[minimum:]
        return merged