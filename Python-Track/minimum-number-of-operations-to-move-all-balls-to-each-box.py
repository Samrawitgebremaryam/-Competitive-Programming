class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result=[]
        for i in range ( len (boxes)):
            distance=0
            for j in range (len(boxes)):
                if i!=j and boxes[j]=="1":
                    distance+=abs(i-j) 
            result.append(distance)
        return result

