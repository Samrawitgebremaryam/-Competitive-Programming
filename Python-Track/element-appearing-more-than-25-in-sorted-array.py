class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count=Counter(arr)
        for i ,n in count.items():
            if n>(len(arr)/4):
                return i
        