class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seat = [0]*(n+1)
        total = 0
        prefix = []

        for i in range (len(bookings)):
            seat[bookings[i][0] -1]+=bookings[i][2]

            seat[bookings[i][1]]-=bookings[i][2]
        for i in range (len(seat)):
            total+=seat[i] 
            prefix.append(total) 
        return prefix[:-1]  

           



        