class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) 
        cou_left = defaultdict(int)
        sum_left = defaultdict(int)

        for i in range (len (nums)):
            ans[i] += (i * cou_left[nums[i]])
            ans[i] -= sum_left[nums[i]]
            sum_left[nums[i]] += i
            cou_left[nums[i]] += 1 


        cou_right = defaultdict(int)
        sum_right = defaultdict(int)

        for i in range (len(nums)-1,-1,-1):
            ans[i] += sum_right[nums[i]]
            ans[i] -= (cou_right[nums[i]] * i)
            
            sum_right[nums[i]] += i
            cou_right[nums[i]] += 1 
        
        return ans




        