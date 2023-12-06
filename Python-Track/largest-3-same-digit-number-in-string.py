class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result=[]
        count=0
        for i in range (len(num)-2):
            if num[i]== num[i+1]==num[i+2]:
                result.append(num[i:i+3])
                count+=1
        if count==0:
            return ''
        else:
            return max(result)
        