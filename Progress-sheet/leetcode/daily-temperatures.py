class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=[] 
        ans=[0]*len(temp)
        for i in range (len(temp)-1,-1,-1):
            while stack and temp[i]>=stack[-1][0]:
                stack.pop()
            if stack :
                ans[i]=stack[-1][1]-i
            stack.append((temp[i],i))
        return ans 


        

























        # l=0
        # r=1
        # ans=[]
        # while l<len(temp)-1:
        #     if temp[r]>temp[l]:
        #         ans.append(r-l)
        #         l+=1
        #         r=l+1
        #     else:
        #         if r<len(temp) :
        #             r+=1
        #         else:
        #             ans.append(0)
        # return ans 
        


        