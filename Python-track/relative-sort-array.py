class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        answer=[]
        not_found=[]
        count = Counter(arr1)
        array2=set(arr2)
        for i in range (len(arr2)):
           answer.extend(([arr2[i]]*count[arr2[i]]))
        
        for i in range (len(arr1)):
            if arr1[i] not in array2:
                not_found.append(arr1[i])
        not_found.sort()
        
        return answer+not_found


        