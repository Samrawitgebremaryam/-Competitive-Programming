class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=length=max_fruit=0
        count=defaultdict(int)
        for r in range (len(fruits)):
            count[fruits[r]]+=1
            length+=1
            while len(count)>2:
                if count[fruits[l]]==1:
                    count.pop(fruits[l])
                else:
                    count[fruits[l]]-=1
                length-=1
                l+=1
            max_fruit=max(max_fruit,length)

        return max_fruit

        