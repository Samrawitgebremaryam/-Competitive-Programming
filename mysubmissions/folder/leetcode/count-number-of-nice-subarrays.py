class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds=count=l=0
        for r in range (len(nums)):
            if nums[r]%2==1:
                odds+=1
            while odds>k:
                if nums[l]%2==1:
                    odds-=1
                l+=1
            if odds == k:
                temp=l
                while nums[temp]%2==0:
                    count += 1
                    temp+=1
                count+=1
        return count














        # count=ans=l=0
        # for r in range (len(nums)):
        #     if nums[r]%2==1:
        #         count+=1
        #     if count==k:
        #         ans+=1 
        #     elif count>k:
                