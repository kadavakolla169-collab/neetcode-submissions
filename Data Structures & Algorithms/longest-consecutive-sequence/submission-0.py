class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set(nums)
        counter = 0
        longest_counter = 0
        for i in nums:
            if i-1 not in sequence:
                start = i
                counter = 1
                while start + 1 in sequence:
                    counter +=1
                    start = start+1
                if counter > longest_counter:
                    longest_counter = counter
        return longest_counter