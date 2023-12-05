class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        result1=''
        result2=''
        for i in range(len(word1)):
            result1+=word1[i]
        for i in range(len(word2)):
            result2+=word2[i]
        return result2==result1
        