class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_indices = [index for index, value in sorted(enumerate(nums), key=lambda x: x[1])]
        sorted_nums = [nums[x] for x in sorted_indices]
        ans = []
        for i in range(len(sorted_nums) - 1):
            org_i = sorted_indices[i]
            need_to_find = target - sorted_nums[i]
            lo = i + 1
            hi = len(sorted_nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if sorted_nums[mid] < need_to_find:
                    lo = mid + 1
                else:
                    hi = mid
            if lo < len(sorted_nums) and sorted_nums[lo] == need_to_find:
                ans.extend([org_i, sorted_indices[lo]]) 
        return sorted(ans)