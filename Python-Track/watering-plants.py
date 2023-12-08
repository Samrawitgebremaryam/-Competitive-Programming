class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count=0
        initial=capacity
        for i in range (len (plants)):
            if capacity<plants[i]:
                count+=(2*i)+1
                capacity=initial
            elif capacity>=plants[i]:
                count+=1
            capacity-=plants[i]
            
        return count 


        