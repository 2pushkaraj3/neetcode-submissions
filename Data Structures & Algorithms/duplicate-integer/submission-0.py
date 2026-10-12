class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ch = 0 
        d ={}
        for x in nums:
            d[x] = d.get(x,0) + 1
            if d[x] > 1:
                return True;
        return False;

          