class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={}
        for i in range (len(order)):
            dic[order[i]]=i
        for i in range(len(words)-1):
            size=min(len(words[i]),len(words[i+1]))
            for j in range (size):
                if dic[words[i][j]]>dic[words[i+1][j]]:
                    return False 
                elif dic[words[i][j]]==dic[words[i+1][j]]:
                    continue
                else:
                    break 
            else:
                if len(words[i])!=size:
                    return False
        return True

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dis={}
        # for i in range(len(order)):
        #        dis[order[i]]=i
        # for i in range(len(words)-1):
        #         size=min(len(words[i]),len(words[i+1]))
        #         for j in range (size):
        #             x=words[i]
        #             y=words[i+1]
        #             if dis[x[j]] < dis[y[j]]:
        #                   break
        #             elif dis[x[j]]==dis[y[j]]:
        #                 continue
        #             else:
        #                 return False
        #         else:
        #             if len(words[i])!=size:
        #                 return False


        return True        

            

