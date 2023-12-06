# class Solution:
#     def printVertically(self, s: str) -> List[str]:
#         s=s.split()
#         result=[]
#         for i in range (len(s[0])):
            # word=''
#             for j in range (len(s)):
#                 word+=s[j][i]
#             result.append(word)
#             
#         return result
class Solution:
    def printVertically(self, s: str):
        words = s.split()
        max_len = max(len(word) for word in words)
        result = []

        for i in range(max_len):
            word = ''
            for j in range(len(words)):
                if i < len(words[j]):
                    word += words[j][i]
                else:
                    word += ' '

            result.append(word.rstrip())  

        return result



        
        