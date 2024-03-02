class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def predict(l,r,turn):
            if turn :
                if l==r:
                    return nums[l]
                left=predict(l+1,r,not turn )+nums[l]
                right=predict(l,r-1 , not turn)+nums[r]
                return max(left,right)
            else:
                if l==r:
                    return -nums[l]
                left =predict (l+1,r,not turn )-nums[l]
                right=predict (l,r-1,not turn )-nums[r]
                return min(left,right)
        return predict (0,len(nums)-1,True)>=0
                
        