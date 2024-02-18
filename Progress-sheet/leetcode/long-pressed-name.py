class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name)>len(typed):
            return False 
        l,r=0,0
        if name [0]!=typed[0]:
            return False 
        while l<len(name) and r<len(typed) :
            if name[l]==typed[r]:
                l+=1
                r+=1
            else:
                if len(typed )>1 and typed[r]==typed[r-1] :
                    r+=1
                else:
                    return False 
        while r<len(typed) and typed[r]==name[-1]  :
            r+=1
        if r<len(typed) or l<len(name):
            return False 
        return True 











    #   real=Counter(name)
    #   fault=Counter(typed)
    #   if len(real)!=len(fault):
    #       return False 
    #   for i in range (len(name)):
    #       if real[name[i]]>fault[name[i]]:
    #           return False
    #   return True 


              
              

           

        