class Solution:
    def arrayChange(self, nums: List[int], operation: List[List[int]]) -> List[int]:
        my_dict={}
        result=[]
        for i in range (len(nums)):
            my_dict[nums[i]]=i
        for ope in operation:
            if ope[0] in my_dict:
                index=my_dict[ope[0]]
                nums[index]=ope[1]
                del my_dict[ope[0]]
                my_dict[ope[1]]=index 
        return (nums) 
    
        