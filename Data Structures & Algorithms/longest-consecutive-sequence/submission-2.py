class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set(nums)
        longest_sequence = 0
        for num in nums:
            if (num-1) not in sequence:
                sequence_length = 1
                while (num + sequence_length) in sequence:
                    sequence_length +=1
                longest_sequence = max(sequence_length, longest_sequence)
        return longest_sequence
