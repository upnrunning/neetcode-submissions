from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        by_frequency = defaultdict(list)
        for num, freq in counts.items():
            by_frequency[freq].append(num)

        ans = []
        for freq in range(len(nums), 0, -1):
            ans.extend(by_frequency[freq])
            if len(ans) >= k:
                return ans