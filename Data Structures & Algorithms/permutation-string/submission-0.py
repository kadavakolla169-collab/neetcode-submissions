class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freqs1 = {}
        for i in s1:
            freqs1[i] = freqs1.get(i, 0) + 1

        freqs2 = {}
        left = 0
        for right in range(len(s2)):
            freqs2[s2[right]] = freqs2.get(s2[right], 0) + 1
            while (right - left + 1) >  len(s1):
                freqs2[s2[left]] -= 1
                if freqs2[s2[left]] == 0:
                    del freqs2[s2[left]]
                left +=1
            if freqs1 == freqs2:
                return True
        return False
                
