class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for idx, value in enumerate(nums):
            if value not in mapping:
                mapping[value] = idx
        for idx, i in enumerate(nums):
            complement = target - i
            if complement in mapping:
                if idx != mapping[complement]: 
                    return sorted([idx, mapping[complement]])
