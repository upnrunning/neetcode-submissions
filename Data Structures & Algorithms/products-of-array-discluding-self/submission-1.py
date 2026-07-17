class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        suffixes = [1]
        ans = []
        for i in range(1, len(nums)):
            prefixes.append(nums[i - 1] * prefixes[i-1])
            suffixes.append(nums[len(nums) - i] * suffixes[i - 1])
        for i in range(len(prefixes)):
            ans.append(prefixes[i] * suffixes[len(suffixes) - 1 - i])
        return ans