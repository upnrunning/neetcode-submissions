from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for elem in nums:
            counts[elem] += 1
        counts = sorted(counts.items(), key=lambda x: -x[1])
        res = []
        for i in range(k):
            res.append(counts[i][0])
        return res