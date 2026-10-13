class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # d= {}
        d = defaultdict(list)
        for x in strs:
            sk = "".join(sorted(x))
            # if sk not in d:
            #     d[sk] = []
            d[sk].append(x)
        return list(d.values())
