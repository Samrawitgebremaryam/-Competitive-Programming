class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total=0
        for i in range(1,len(salary)-1):
            total+=salary[i]
        avarage=total/(len(salary)-2)
        return avarage

        