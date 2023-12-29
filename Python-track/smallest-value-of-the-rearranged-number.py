class Solution:
    def smallestNumber(self, num: int) -> int:
        
        nums=str(num)
        count=0
  
        if num>0:
            nums=list(map(int,nums))
            nums.sort()
            for i in range (len (nums)):
                if nums[i]==0:
                    count+=1
                else:
                    break
        
            nums[count],nums[0]=nums[0],nums[count]
            numbers=list(map(str,nums)) 
            return int("".join(numbers))
        elif num==0:
            return 0   
        else:
            nums=list(map(int,nums[1:]))
            nums.sort(reverse=True)
            numbers=list(map(str,nums)) 
            return -int("".join(numbers))

        
        





