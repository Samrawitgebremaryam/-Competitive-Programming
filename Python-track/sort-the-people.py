class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #  Bubble sort 
        # for i in range(len(names)):
        #     for j in range(len(names)-i-1):
        #         if heights[j]<heights[j+1]:
        #             heights[j],heights[j+1]=heights[j+1],heights[j]
        #             names[j],names[j+1]=names[j+1],names[j]         
        # return names


        # Selection sort 
        for i in range (len(names)) :
            max_index=i
            for j in range(i+1,len(names)):
                if heights[j]>heights[max_index]:
                    max_index=j
            heights[i],heights[max_index]=heights[max_index],heights[i]
            names[i],names[max_index]=names[max_index],names[i]  
        return names

                
