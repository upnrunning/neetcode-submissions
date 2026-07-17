class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        has_zeros = False
        total_cumulative = 1
        ans = []
        for num in nums:
            if num == 0:
                if not has_zeros:
                    has_zeros = True
                    continue
                else:
                    return [0] * len(nums)
            total_cumulative *= num
        for num in nums:
            if has_zeros:
                if num != 0:
                    ans.append(0)
                else:
                    ans.append(total_cumulative)
            else:
                ans.append(total_cumulative // num)
        return ans