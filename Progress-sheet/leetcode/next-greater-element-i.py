class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count={}
        ans=[]
        stack=[]
        for i in range (len (nums1)):
            count[nums1[i]]=-1

        for i in range (len(nums2)):
            while stack and nums2[i]> stack[-1]:
                if stack and (stack[-1] in count):
                    count[stack[-1]]= nums2[i]
                stack.pop() 
                
            stack.append(nums2[i])
        print(count)
        for i in count.values():
            ans.append(i)

        return ans 
    


        