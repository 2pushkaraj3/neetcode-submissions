class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = 0 
        d = []
        for i in range(len(nums)):
            t = target - nums[i]
            d.append(i)
            for j in range(i+1,len(nums)):
                if t-nums[j] == 0:
                    d.append(j)
                    return d
            d.clear()
        
        return d
            
        


#         Line 4 with lines 10 and 13: wrong type. {} is a dict, and dicts have no .append, so line 10 throws an AttributeError. What empty literal gives you something with .append?
# Lines 7–8: a wrong assumption. Why would t < 0 mean there’s no answer? The array can contain negative numbers. Trace it with nums = [-1, 5] and target = 4.


