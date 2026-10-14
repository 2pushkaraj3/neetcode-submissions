class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        # print("cnt -",cnt)
        ans = cnt.most_common(k)
        # print("ans -",ans)
        d = []
        for x in ans:
            d.append(x[0])
        return d

        