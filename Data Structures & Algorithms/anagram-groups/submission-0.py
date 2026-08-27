class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_res = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            final_res[sorted_s].append(s)
        return list(final_res.values())