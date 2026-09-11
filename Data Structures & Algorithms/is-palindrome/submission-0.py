class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        s2 = ""
        s=s.lower()
        for i in s:
            if i.isalnum():
                s1 = s1+i
        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum():
                s2 = s2+s[i]
        if s1 == s2:
            return True
        return False
