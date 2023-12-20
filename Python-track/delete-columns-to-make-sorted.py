class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for word in (zip(*strs)):
            for j in range(len(word)-1):
                if word[j] > word[j + 1]:
                    count += 1 
                    break
       
        return count
   
            

            
        
        