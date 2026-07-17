class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {} # (tuple) -> [tuple_1, tuple2, ...]
        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord('a')] += 1
            freq = tuple(freq)
            if freq in result:
                result[freq].append(string)
            else:
                result[freq] = [string]
        return list(result.values())