class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        my_dict=dict(zip(indices,s))
        my_dict=dict(sorted(my_dict.items()))
        result=''
        for values in my_dict.values():
            result+=values
        return result