class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwise=0
        total=0
        anticlock=0

        for i in range (len(distance)):
            total+=distance[i]
        if start<destination:
            for i in range (start,destination):
                clockwise+=distance[i]
        else:
            for i in range (destination,start):
                clockwise+=distance[i]

        anticlock=total-clockwise
        
        return min(clockwise,anticlock)
