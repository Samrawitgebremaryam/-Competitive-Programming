class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        max_time=0
        processorTime.sort()
        tasks.sort(reverse=True)
        n=0
        for i in range (len(tasks)):
            max_time=max(tasks[i]+processorTime[n],max_time)
            if ((i+1)%4)==0:
                n+=1
        return max_time
            


        