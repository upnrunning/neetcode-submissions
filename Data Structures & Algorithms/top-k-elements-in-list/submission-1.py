from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        reverse_count = defaultdict(list)
        for i, j in counts.items():
            reverse_count[j].append(i)
        ans = []
        for i in range(1000, -1001, -1):
            if i in reverse_count:
                ans.extend(reverse_count[i])
            if len(ans) >= k:
                return ans
        return ans