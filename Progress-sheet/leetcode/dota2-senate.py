class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d , r = deque() , deque ()
        n = len(senate)
        
        for i in range (len (senate)):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)
        
        while r and d :
            if d.popleft() < r.popleft() :
                d.append(n)
            else:
                r.append(n)
            n += 1
        return "Radiant" if r else "Dire"










        # senate = deque(sen)
        # count = Counter (sen) 
        # flagr = 0 
        # flagd = 0 
        # while len(senate) != 1 :

        #     if senate[0] == "R" and flagr > 0 :
        #         senate.popleft()
        #     elif senate[0] == "D" and flagd >0 :
        #         senate.popleft()

        #     if senate[0] == "R" and senate[1] == "D" or senate[0] == "D" and senate[1] == "R" :
        #         x = senate.popleft() 
        #         senate.append(x)
        #         y = senate.popleft()
        #         count[y] -= 1
        #     else : 
        #         x = senate.popleft()  
        #         senate.append(x)
        #         if x == "R" and count["D"] > 0 :
        #             count["D"] -= 1
        #             flagd += 1
        #         elif x == "D" and count["R"] > 0:
        #             count["R"] -= 1 
        #             flagr += 1

        # if count["R"] > count ["D"] :
        #     return "Radiant" 
        # else:
        #     return "Dire"

            
            