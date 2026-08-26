class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first_string=strs[0]
        last_string=strs[-1]
        i=0
        while i<len(first_string) and i<len(last_string) and first_string[i]==last_string[i]:
            i+=1
        return first_string[:i]