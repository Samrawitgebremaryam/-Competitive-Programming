class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        my_dict={place:index for index,place in enumerate (list1) }
        mini=float("inf")
        result=[]
        current=0
        for i , resturant in enumerate (list2):
            if resturant in my_dict:
                current=i+my_dict[resturant]
                if current<mini:
                    mini=current
                    result=[resturant]
                elif current ==mini:
                    result.append(resturant)
        return result
                
            

        